from django.urls import path
from . import views

app_name = 'bestiario'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('criatura/<int:id>/', views.detalle, name='detalle'),
    path('reportar/', views.reportar, name='reportar'),
]