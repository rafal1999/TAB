"""tab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Site import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('testworkers/', views.test_workers_page, name='testworkers'),
    path('testcandidates/',views.test_candidates_page, name='testcandidates'),
    path('testcalendar/', views.test_calendar_page, name='testcalendar'),
    path('index/', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
