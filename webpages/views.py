import requests
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from webpages import utils

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENTDIR = [os.path.join(BASE_DIR, 'webpages/templates/')]

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
        print("DEBUG:views.py.home")
        print("views.py.home().CONTENTDIR=", CONTENTDIR)
        
    context = {
        'links':utils.getFileNames(CONTENTDIR),
        'title':'Home',
    }
    return render(request, 'home.html', context)


def projects(request):
    
    if (utils.DEBUG):
        print("DEBUG:views.py.projects")   

    # Combine Django with GitHub API
    response = requests.get('https://api.github.com/users/lisasboylanportfolio/repos')
    repos = response.json()
    if utils.DEBUG:
        print("DEBUG:views.py.projects.repos=", repos)        

    context = {
        'links':utils.getFileNames(CONTENTDIR),
        'title':'Projects',
        'github_repos': repos,        
    }
    return render(request, 'projects.html', context)
