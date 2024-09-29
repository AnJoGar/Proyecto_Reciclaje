"""
URL configuration for proyecto_reciclaje project.

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
from django.urls import path
from red_neuronal.views import PredecirResiduosView # Importa correctamente desde el archivo views.py
from cantidad_residuos_actuales.views import obtener_estadisticas
urlpatterns = [
     path('predecir_residuos/', PredecirResiduosView.as_view(), name='predecir_residuos'), 
        path('obtener_estadisticas/', obtener_estadisticas, name='obtener_estadisticas'), # Define la URL
]