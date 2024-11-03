# principal/urls.py
from django.contrib import admin
from django.urls import path, include
from inicio import views as inicio  # Importa las vistas de la aplicación 'inicio'

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', inicio.login_view, name='login'),  # URL para la vista de login
    path('logout/', inicio.logout_view, name='logout'),  # URL para la vista de logout
    path('menu/', inicio.menu_view, name='menu'),  # URL para la vista del menú
    path(
        "pacientes/",
        include([
            path("ver/", inicio.ver_pacientes, name='ver_pacientes'),
            path("agregar/", inicio.agregar_pacientes, name='agregar_pacientes'),
            path("modificar/", inicio.modificar_pacientes, name='modificar_pacientes'),
            path("eliminar/", inicio.eliminar_pacientes, name='eliminar_pacientes'),
            path('eliminar/', inicio.eliminar_paciente, name='eliminar_paciente'),
            path('buscar/', inicio.buscar_paciente, name='buscar_paciente'),
            path('paciente/', inicio.actualizar_paciente, name='actualizar_paciente'),


        ])),
    
    path("citas/", include([
        path("ver/", inicio.ver_citas),
        path("programar/", inicio.programar_citas, name='programar_citas'),
        path("reprogramar/", inicio.reprogramar_citas, name='reprogramar_citas'),
        path("cancelar/", inicio.cancelar_citas, name='cancelar_citas'),
        path("eliminar/", inicio.eliminar_pacientes, name='eliminar_citas'),
        path("buscar_cita/", inicio.buscar_cita, name='buscar_cita'),  # Nueva ruta
    ])),
    
    path('ver_consultorios/', inicio.ver_consultorios, name='consultorios'),
    
    #path('buscar_paciente/', inicio.buscar_paciente, name='buscar_paciente'),

    #path('actualizar_paciente/', inicio.actualizar_paciente, name='actualizar_paciente'),

    #path('eliminar/', inicio.eliminar_paciente, name='eliminar_paciente'),
    #path('buscar/', inicio.buscar_paciente, name='buscar_paciente'),

    #path('buscar_cita', inicio.buscar_cita, name='buscar_cita'),
    #path('citas/programar/', inicio.programar_citas, name='programar_citas'),

    path('reset-password/', inicio.restablecer_view, name='reset_password'),

    path(
        "reportes/",
        include(
            [
                path("generar/", inicio.generar_reportes),
                path("enviar/", inicio.enviar_reporte),

            ]
        ),
    ),
    
    path(
        "expedientes/",
        include(
            [
                path("crear/", inicio.crear_expediente),
                path("modificar/", inicio.modificar_expediente),
                path("ver/", inicio.ver_expediente),
                path("eliminar/", inicio.eliminar_expediente),
            ]
        ),
    ),
    
    path('volver/', inicio.volver, name='volver'),

    #path('buscar_cita/', inicio.buscar_cita, name='buscar_cita'),
    #path('citas/programar/', inicio.programar_cita, name='programar_cita'),  
]
