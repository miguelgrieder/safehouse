from django.urls import path
from . import views

urlpatterns = [
    path('', views.getImovel),
    path('addImovel', views.addImovel),
    path('getAcionamento', views.getAcionamento),
    path('addAcionamento', views.addAcionamento),
    path('getStatus', views.getStatus),
    path('addStatus', views.addStatus),
    path('getSensor', views.getSensor),
    path('addSensor', views.addSensor),
    path('getNotificacao', views.getNotificacao),
    path('addNotificacao', views.addNotificacao),
]