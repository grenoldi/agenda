"""agenda URL Configuration

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
from django.urls import path
# from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('eventos/<titulo_evento>', views.get_local),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/', views.json_lista_eventos),
    path('agenda/evento/', views.registrar_evento),
    path('agenda/evento/submit', views.submeter_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.apagar_evento),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    # path('', RedirectView.as_view(url='/agenda/'))
]
