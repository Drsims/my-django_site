from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm
from .utils import paginateProjects, SearchProjects


def index(request):
    projects, search_query = SearchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context = {'index':projects, 'projects':projects, 'custom_range':custom_range}
    return render(request, 'users/index.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project':projectObj}
    return render(request, 'users/project.html',context)

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'users/forms.html', context)

def updateProject(request, pk):
    project= Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'users/forms.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method =='POST':
        project.delete()
        return redirect('index')
    

    context = {'object':project}
    return render(request,'users/delete_template.html', context)