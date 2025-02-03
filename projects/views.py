from django.shortcuts import render, redirect
from .models import Project
from .form import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context=context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()

    context = {"project": project, "tags": tags}
    return render(request, "projects/single-project.html", context=context)


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": ProjectForm}
    return render(request, "projects/project_form.html", context=context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context=context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "projects/delete_template.html", context=context)
