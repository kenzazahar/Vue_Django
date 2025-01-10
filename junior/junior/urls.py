"""
URL configuration for junior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from apps.core.views import *
from apps.store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('register/student/', register_student, name='register_student'),
    path('register/company/', register_company, name='register_company'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'), 
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('add-job-offer/', add_job_offer, name='add_job_offer'),
    path('job-offers-list/', job_offer_list, name='job_offer_list'),
    path('All-Jobs/', List_AllJobs, name='List_AllJobs'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('search-bar/', search_bar, name='search_bar'),
    path('jobs/<int:job_id>/apply/', apply_to_job, name='apply_to_job'),
]
print("URL patterns:", urlpatterns)