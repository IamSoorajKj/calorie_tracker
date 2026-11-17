"""
URL configuration for calorie_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from accounts.views import SignUpView

from calorie_management.views import CalorieListCreateView
from calorie_management.views import CalorieRetrieveUpdateDeleteView
from calorie_management.views import CalorieSummaryView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts

    path('accounts/register/',SignUpView.as_view()),

    #calorie
    path('calories/',CalorieListCreateView.as_view()),
    path('calories/add/',CalorieListCreateView.as_view()),

    path('calories/<int:pk>/',CalorieRetrieveUpdateDeleteView.as_view()),

    #calorie summary
    path('calories/summary/',CalorieSummaryView.as_view()),

    #token generation

    path('token/',ObtainAuthToken.as_view()),
]
