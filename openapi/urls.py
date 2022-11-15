from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ApiDocView,
    ApiSpecificationView,
    ApiSpecificationOnlyView,
    ApiDocEditView,
    ApiDocEdit,
    CreateApiSpecification,
    DeleteApiSpecification,
)

urlpatterns = [
    path("docs/<uuid:id>", login_required(ApiDocView.as_view()), name="doc_view"),
    path(
        "docs/<uuid:id>/edit",
        login_required(ApiDocEditView.as_view()),
        name="doc_edit_view",
    ),
    path("docs/edit", login_required(ApiDocEdit.as_view()), name="doc_edit"),
    path(
        "specs/<uuid:id>", login_required(ApiSpecificationView.as_view()), name="spec"
    ),
    path(
        "specs_only/<uuid:id>",
        login_required(ApiSpecificationOnlyView.as_view()),
        name="spec_only",
    ),
    path(
        "spec/create",
        login_required(CreateApiSpecification.as_view()),
        name="spec_create",
    ),
    path(
        "spec/<uuid:id>/delete",
        login_required(DeleteApiSpecification.as_view()),
        name="spec_delete",
    ),
]
