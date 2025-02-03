from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["featured_image", "title", "description", "demo_link", "source_link", "tags"]
