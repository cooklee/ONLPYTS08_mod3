"""OnlPysS08 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pierwsza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('przywitanie/<str:imie>/', views.przywitanie),
    path('ala/', views.ala),
    path('losuj/<int:liczba>/', views.losuj),
    path('dodaj/<int:l1>/<int:l2>/', views.dodaj),
    path('l_parametr/', views.losuj_parametr),
    path('get/', views.pokaz_parametry_get),
    path('tab/<int:a>/<int:b>/', views.tabliczka_mnozenia),
    path('add_person/', views.add_person),
    path('all_person/', views.all_persons),
    path('person_detail/<int:id>/', views.person_detail),
    path('update_person/<int:id>/', views.update_person)
]
