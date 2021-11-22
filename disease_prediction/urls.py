"""disease_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from predict import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('prediction/', views.prediction, name="prediction"),
    path('report/', views.report, name="report"),
    path('myReports/', views.myReports, name="myReports"),
    path('report/<int:report_pk>', views.viewreport, name='viewreport'),
    path('printreport/', views.printreport, name="printreport"),

    # Auth
    path('', TemplateView.as_view(template_name="predict/index.html")),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name="loginuser"),
    path('logout/', views.logoutuser, name="logoutuser"),

    #Searchbar
    # path('seachbar/', views.seachbar, name="seachbar"),
    path('disease_search/', views.disease_search, name="disease_search"),
    path('doctor_search/', views.doctor_search, name="doctor_search"),
    path('doctor_found/', views.doc_querry, name="doc_querry"),

    #blog
    path('blog/', include('blog.urls')),
]
