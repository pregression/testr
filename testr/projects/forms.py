from django.forms import ModelForm, CharField, HiddenInput
from .models import Project


class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        # name = forms.CharField(
        #     widget=forms.TextInput(attrs={'class': 'CreateProjectForm--inputGroupInput'}),
        #     label="Project Name"
        # )
