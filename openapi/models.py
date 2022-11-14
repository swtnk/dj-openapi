from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid


def get_specification_placeholder():
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "TITLE",
            "description": "DESCRIPTION",
            "termsOfService": "LINK.com",
            "contact": {"email": "EMAIL@EXAMPLE.COM"},
            "license": {"name": "LICENSE", "url": "LINK-TO-LICENCE.COM"},
            "version": "VERSION",
        },
        "externalDocs": {
            "description": "EXTERNAL DESCRIPTION",
            "url": "LINK-TO-EXTERNAL-DESCRIPTION.COM",
        },
        "servers": [{"url": "https://link-to-server.com/"}],
        "tags": [
            {
                "name": "tag-1",
                "description": "Tag 1 description",
                "externalDocs": {
                    "description": "External Description",
                    "url": "link-to-external-description.com",
                },
            }
        ],
        "paths": {
            "/path-1": {
                "get": {
                    "tags": ["tag-1"],
                    "summary": "Get tag-1",
                    "description": "Multiple status values can be provided with comma separated strings",
                    "operationId": "findPetsByStatus",
                    "parameters": [
                        {
                            "name": "status",
                            "in": "query",
                            "description": "Status values that need to be considered for filter",
                            "required": False,
                            "explode": True,
                            "schema": {
                                "type": "string",
                                "default": "available",
                                "enum": ["available", "pending", "sold"],
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Tag"},
                                    }
                                },
                                "application/xml": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Tag"},
                                    }
                                },
                            },
                        },
                        "400": {"description": "Invalid status value"},
                    },
                    "security": [{"example_auth": ["write:tag", "read:tag"]}],
                },
                "post": {
                    "tags": ["tag-1"],
                    "summary": "Add a new tag-1",
                    "description": "Description for adding a new tag-1",
                    "operationId": "addTag",
                    "requestBody": {
                        "description": "Create a new tag in the store",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Tag"}
                            },
                            "application/xml": {
                                "schema": {"$ref": "#/components/schemas/Tag"}
                            },
                            "application/x-www-form-urlencoded": {
                                "schema": {"$ref": "#/components/schemas/Tag"}
                            },
                        },
                        "required": True,
                    },
                    "responses": {
                        "200": {
                            "description": "Successful operation",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Tag"}
                                },
                                "application/xml": {
                                    "schema": {"$ref": "#/components/schemas/Tag"}
                                },
                            },
                        },
                        "405": {"description": "Invalid input"},
                    },
                    "security": [{"example_Auth": ["write:tag", "read:tag"]}],
                },
            }
        },
        "components": {
            "schemas": {
                "Tag": {
                    "required": ["name", "photoUrls"],
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "format": "int64", "example": 10},
                        "name": {"type": "string", "example": "doggie"},
                        "photoUrls": {
                            "type": "array",
                            "xml": {"wrapped": True},
                            "items": {"type": "string", "xml": {"name": "photoUrl"}},
                        },
                        "tags": {
                            "type": "array",
                            "xml": {"wrapped": True},
                            "items": {"$ref": "#/components/schemas/Tag"},
                        },
                        "status": {
                            "type": "string",
                            "description": "tag status in the store",
                            "enum": ["available", "pending", "sold"],
                        },
                    },
                    "xml": {"name": "tag"},
                },
                "User": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "format": "int64", "example": 10},
                        "username": {"type": "string", "example": "theUser"},
                        "firstName": {"type": "string", "example": "John"},
                        "lastName": {"type": "string", "example": "James"},
                        "email": {"type": "string", "example": "john@email.com"},
                        "password": {"type": "string", "example": "12345"},
                        "phone": {"type": "string", "example": "12345"},
                        "userStatus": {
                            "type": "integer",
                            "description": "User Status",
                            "format": "int32",
                            "example": 1,
                        },
                    },
                    "xml": {"name": "user"},
                },
            },
            "requestBodies": {
                "Tag": {
                    "description": "Tag object that needs to be added to the store",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Tag"}
                        },
                        "application/xml": {
                            "schema": {"$ref": "#/components/schemas/Tag"}
                        },
                    },
                },
                "UserArray": {
                    "description": "List of user object",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/User"},
                            }
                        }
                    },
                },
            },
            "securitySchemes": {
                "example_auth": {
                    "type": "oauth2",
                    "flows": {
                        "implicit": {
                            "authorizationUrl": "https://authorization-url.example.com",
                            "scopes": {
                                "write:tags": "modify tags in your account",
                                "read:tags": "read your tags",
                            },
                        }
                    },
                },
                "api_key": {"type": "apiKey", "name": "api_key", "in": "header"},
            },
        },
    }


# Create your models here.
class ApiSpecification(models.Model):
    class Meta:
        db_table = "api_specification"
        ordering = ["-updated_at"]

    id = models.UUIDField(
        verbose_name=_("id"), primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(
        verbose_name=_("title"),
        max_length=255,
        blank=False,
        null=False,
        help_text="API Title",
    )
    description = models.TextField(
        verbose_name=_("description"),
        blank=True,
        null=True,
        help_text="API Description",
    )
    specification = models.JSONField(
        verbose_name=_("specification"),
        blank=True,
        null=True,
        help_text="API Specification",
        default=get_specification_placeholder,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
        editable=False,
        help_text="Created At",
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
        help_text="Updated at",
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name="spec_created_by",
        null=True,
        blank=True,
    )
    users = models.ManyToManyField(to=User, related_name="accessible_to")

    def __str__(self) -> str:
        return f"{self.title} - {self.id}"
