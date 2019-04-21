"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls    import include, path
from django.conf    import settings

from webpages import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('abilities/', views. abilities),
    path('projects/', views.projects),
    path('delete-project/<project_id>/', views.delete_project),
    path('edit-project/<project_id>/', views.edit_project),
    path('create-project/', views.create_project),        
    path('admin/', admin.site.urls),
]

# NOTE: To get media working, we need to do something like this. See
# also the end of the settings.py file.
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)