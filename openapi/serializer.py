from config.serializers import DynamicFieldsModelSerializer
from rest_framework import serializers
from .models import ApiSpecification


class ApiSpecificationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ApiSpecification
        fields = "__all__"
