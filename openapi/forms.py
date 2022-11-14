from prettyjson import PrettyJSONWidget
from django import forms
from .models import ApiSpecification


class JsonForm(forms.ModelForm):
    class Meta:
        model = ApiSpecification
        fields = "__all__"
        widgets = {
            "specification": PrettyJSONWidget(),
        }
