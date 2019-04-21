import requests
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms

from webpages import utils

from .models import Projects

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENTDIR = [os.path.join(BASE_DIR, 'webpages/templates/')]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['image', 'name',  'desc', 'link']
                  
def abilities(request):

    if (utils.DEBUG):
        print("DEBUG:views.py.abilities")  

    context = {
        'links':utils.getFileNames(CONTENTDIR),
        'title':'Projects',
    }
    return render(request, 'abilities.html', context)

def home(request):
    
    if (utils.DEBUG):
        print(
            "DEBUG:views.py.home")
        print("views.py.home().CONTENTDIR=", CONTENTDIR)
        
    context = {
        'links':utils.getFileNames(CONTENTDIR),
        'title':'Home',
    }
    return render(request, 'home.html', context)


def projects(request):
    
    if (utils.DEBUG):
        print("DEBUG:views.py.projects")   

    # CREATE projects
    if request.method == 'POST':
        if utils.DEBUG:
            print("DEBUG:views.py.projects.POST") 

        # Create a form instance and populate it with data from the request,
        # including uploaded files
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            # Use the form to save
            form.save()

            # Cool trick to redirect to the previous page
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        # Combine Django with GitHub API
        # response = requests.get('https://api.github.com/users/lisasboylanportfolio/repos')
        # repos = response.json()
        if utils.DEBUG:
            print("DEBUG:views.py.projects.GET")
            
        # if a GET we'll create a blank form
        form = ProjectForm()
        
        projects = Projects.objects.all()
    
        context = {
            'links':utils.getFileNames(CONTENTDIR),
            'title':'Projects',
            'projects': projects,
            'form' : form,
        }
        return render(request, 'projects.html', context)

def like_project(request, project_id):
    # Update the tweet to add the user as "liked"
    Projects.objects.get(pk=project_id).update(likes=F('likes') + 1)
    

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_project(request, project_id):
    if utils.DEBUG:
         print("DEBUG:views.py.delete_project")
         
    project = Projects.objects.get(id=project_id)
    project.delete()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))

def edit_project(request, project_id):
    if utils.DEBUG:
         print("DEBUG:views.py.edit_project")

    # Update the project
    project = Projects.objects.get(id=project_id)    
    project.name = request.POST['name']
    project.desc = request.POST['desc']
    project.link = request.POST['link']
    project.image = request.POST['image'] 

    project.save()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))         

def create_project(request):
    if utils.DEBUG:
         print("DEBUG:views.py.create_project")
            
    # Create a form instance and populate it with data from the request
    form = ProjectForm(request.POST)

    if form.is_valid():
        if utils.DEBUG:
            print("DEBUG:views.py.create_project.form.isValid")            
        form.save()
        # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))