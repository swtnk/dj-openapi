from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ApiSpecification
from .serializer import ApiSpecificationSerializer
from django.urls import reverse
from django.utils.decorators import method_decorator
import json

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {"page": "Login"}
        return render(request=request, template_name="login.html", context=context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {
                "status": False,
                "message": "Invalid Credentials",
                "page": "Login",
            }
            return render(request=request, template_name="login.html", context=context)
        login(request, user)
        redirect_to = request.GET.get("next", reverse("dashboard"))
        return redirect(redirect_to)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request=request)
        return redirect(reverse("dashboard"))


class SpecificationLists(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            specification = ApiSpecification.objects.all()[:10]
        else:
            specification = ApiSpecification.objects.filter(
                Q(users=request.user) | Q(created_by=request.user)
            )[:10]

        context = {
            "specifications": specification,
            "page": "Dashboard",
        }
        return render(request=request, template_name="home.html", context=context)


class CreateApiSpecification(View):
    def post(self, request, *args, **kwargs):
        request_data = request.POST
        title = request_data.get("title")
        description = request_data.get("description")
        specification = json.loads(request_data.get("specification"))
        data = {
            "title": title,
            "description": description,
            "specification": specification,
            "created_by": request.user.id,
            "users": [request.user.id],
        }
        serializer = ApiSpecificationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {
                "status": "success",
                "message": "Specification Created",
                "data": serializer.data,
            }
            return JsonResponse(data=response_data)
        else:
            return JsonResponse(
                data={"status": "failed", "message": "Failed to create specification"}
            )


class DeleteApiSpecification(View):
    def get(self, request, *args, **kwargs):
        specification_id = kwargs.get("id")
        specification_object = ApiSpecification.objects.filter(id=specification_id)
        if specification_object.exists():
            specification = specification_object.first()
            # print(request.user, specification.users.filter(id=request.user.id))
            # if request.user.is_superuser or specification.accessible_to.filter(user=request.user).exists():
            specification.delete()
        return redirect("dashboard")


class ApiDocView(View):
    def get(self, request, *args, **kwargs):
        url = reverse("spec_only", kwargs={"id": kwargs.get("id", "")})
        context = {"spec_url": url, "page": "Viewer"}
        style = request.GET.get("style")
        template = "swagger-ui.html"
        if style == "redoc":
            template = "redocly.html"
        return render(request=request, template_name=template, context=context)


class ApiSpecificationView(APIView):
    def get(self, request, *args, **kwargs):
        specification_id = kwargs.get("id", None)
        specification_object = ApiSpecification.objects.filter(id=specification_id)
        serializer = ApiSpecificationSerializer(specification_object, many=True)
        return Response(data=serializer.data)


class ApiSpecificationOnlyView(APIView):
    def get(self, request, *args, **kwargs):
        specification_id = kwargs.get("id", None)
        specification_object = ApiSpecification.objects.filter(id=specification_id)
        if specification_object.exists():
            return JsonResponse(data=specification_object[0].specification)
        return Response(data={})


class ApiDocEditView(View):
    def get(self, request, *args, **kwargs):
        specification_id = kwargs.get("id", None)
        specification_object = ApiSpecification.objects.filter(id=specification_id)
        serializer = ApiSpecificationSerializer(specification_object, many=True)
        context = {
            "spec_url": reverse("spec", kwargs={"id": specification_id}),
            "data": serializer.data,
            "page": "Editor",
        }
        return render(
            request=request, template_name="swagger-ui-edit.html", context=context
        )


class ApiDocEdit(APIView):
    def post(self, request, *args, **kwargs):
        specification_id = request.POST.get("id")
        specification_object = ApiSpecification.objects.filter(id=specification_id)
        if specification_object.exists():
            serializer = ApiSpecificationSerializer(
                specification_object.first(), data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data, "message": "updated"}
                )
        return Response({"status": "failed", "message": "invalid request"})
