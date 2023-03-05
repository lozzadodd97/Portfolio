from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from portfolio_content.models import Project

def project_index(request):
    """An index view that shows a snippet of information about each project"""
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """A detail view that shows more information on a particular topic"""
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
