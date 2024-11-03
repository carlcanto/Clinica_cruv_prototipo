from django.urls import path
from .views import login_view, menu_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('menu/', menu_view, name='menu'),
    path('logout/', logout_view, name='logout'),
    #path('verpacientes/', ver_pacientes, name='verpacientes'),
]
