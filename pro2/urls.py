"""
URL configuration for pro2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import ListView, DetailView
from lab8.models import Student

student_list_info = {
    "model": Student,
    "context_object_name": "student_list",  # Ensure this matches the template variable
    "template_name": "student_list.html"
}

student_detail_info = {
    "model": Student,
    "context_object_name": "student",  # Ensure this matches the template variable
    "template_name": "student_detail.html"
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', ListView.as_view(**student_list_info), name='student_list'),
    path('student_detail/<int:pk>/', DetailView.as_view(**student_detail_info), name='student_detail'),
]

