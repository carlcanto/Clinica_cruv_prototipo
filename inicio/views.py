# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from historial.models import Pacientes, Citas
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import random
import string
from .forms import CitaForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
    return render(request, 'inicio/login.html')

@login_required
def menu_view(request):
    return render(request, 'inicio/menu.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def ver_pacientes(request):
    return render(request, 'inicio/pacientes/ver-pacientes.html')

def agregar_pacientes(request):
    if request.method == 'POST':
        id_paciente = request.POST.get('id_paciente')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        cedula = request.POST.get('cedula')
        seguro_social = request.POST.get('seguro_social')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        lugar_de_trabajo = request.POST.get('lugar_de_trabajo')
        ocupacion = request.POST.get('ocupacion')
        direccion_trabajo = request.POST.get('direccion_trabajo')
        telefono_trabajo = request.POST.get('telefono_trabajo')
        persona_emergencia = request.POST.get('persona_emergencia')
        telefono_emergencia = request.POST.get('telefono_emergencia')
        direccion_emergencia = request.POST.get('direccion_emergencia')
        relacion_emergencia = request.POST.get('relacion_emergencia')

        Pacientes.objects.create(
            id_paciente=id_paciente,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            sexo=sexo,
            cedula=cedula,
            seguro_social=seguro_social,
            direccion=direccion,
            telefono=telefono,
            lugar_de_trabajo=lugar_de_trabajo,
            ocupacion=ocupacion,
            direccion_trabajo=direccion_trabajo,
            telefono_trabajo=telefono_trabajo,
            persona_emergencia=persona_emergencia,
            telefono_emergencia=telefono_emergencia,
            direccion_emergencia=direccion_emergencia,
            relacion_emergencia=relacion_emergencia
        )
    return render(request, 'inicio/pacientes/agregar-paciente.html')

def modificar_pacientes(request):
        
    return render(request, 'inicio/pacientes/modificar-paciente.html')

def eliminar_pacientes(request):
    return render(request, 'inicio/pacientes/eliminar-paciente.html')


def reprogramar_citas(request):
    return render(request, 'inicio/citas/reprogramar_cita.html')

def cancelar_citas(request):
    return render(request, 'inicio/citas/cancelar_cita.html')

def ver_citas(request):
    return render(request, 'inicio/citas/ver_citas.html')

def ver_consultorios(request):
    return render(request, 'inicio/consultorio/ver_consultorio.html')

def programar_citas(request):
    return render(request, 'inicio/citas/programar_cita.html')

def generar_reportes(request):
    return render(request, 'inicio/reportes/generar_reporte.html')

def enviar_reporte(request):
    return render(request, 'inicio/reportes/enviar_reporte.html')

def crear_expediente(request):
    return render(request, 'inicio/expedientes/crear_expediente.html')

def eliminar_expediente(request):
    return render(request, 'inicio/expedientes/eliminar_expediente.html')

def modificar_expediente(request):
    return render(request, 'inicio/expedientes/modificar_expediente.html')

def ver_expediente(request):
    return render(request, 'inicio/expedientes/ver_expediente.html')

def volver(request):
    return render(request, 'inicio/menu.html')

@csrf_exempt
def buscar_paciente(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        try:
            paciente = Pacientes.objects.get(cedula=cedula)
            data = {
                'id_paciente': paciente.id_paciente,
                'nombre': paciente.nombre,
                'apellido': paciente.apellido,
                'fecha_nacimiento': paciente.fecha_nacimiento,
                'edad': paciente.edad,
                'sexo': paciente.sexo,
                'cedula': paciente.cedula,
                'seguro_social': paciente.seguro_social,
                'direccion': paciente.direccion,
                'telefono': paciente.telefono,
                'lugar_de_trabajo': paciente.lugar_de_trabajo,
                'ocupacion': paciente.ocupacion,
                'direccion_trabajo': paciente.direccion_trabajo,
                'telefono_trabajo': paciente.telefono_trabajo,
                'persona_emergencia': paciente.persona_emergencia,
                'telefono_emergencia': paciente.telefono_emergencia,
                'direccion_emergencia': paciente.direccion_emergencia,
                'relacion_emergencia': paciente.relacion_emergencia,
            }
            return JsonResponse(data)
        except Pacientes.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado.'}, status=404)
        
@csrf_exempt
def actualizar_paciente(request):
    if request.method == 'POST':
        id_paciente = request.POST.get('id_paciente')
        try:
            paciente = Pacientes.objects.get(id_paciente=id_paciente)
            paciente.nombre = request.POST.get('nombre')
            paciente.apellido = request.POST.get('apellido')
            paciente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            paciente.edad = request.POST.get('edad')
            paciente.sexo = request.POST.get('sexo')
            paciente.cedula = request.POST.get('cedula')
            paciente.seguro_social = request.POST.get('seguro_social')
            paciente.direccion = request.POST.get('direccion')
            paciente.telefono = request.POST.get('telefono')
            paciente.lugar_de_trabajo = request.POST.get('lugar_de_trabajo')
            paciente.ocupacion = request.POST.get('ocupacion')
            paciente.direccion_trabajo = request.POST.get('direccion_trabajo')
            paciente.telefono_trabajo = request.POST.get('telefono_trabajo')
            paciente.persona_emergencia = request.POST.get('persona_emergencia')
            paciente.telefono_emergencia = request.POST.get('telefono_emergencia')
            paciente.direccion_emergencia = request.POST.get('direccion_emergencia')
            paciente.relacion_emergencia = request.POST.get('relacion_emergencia')
            paciente.save()
            return JsonResponse({'success': 'Paciente actualizado correctamente.'})
        except Pacientes.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado.'}, status=404)
@csrf_exempt
def eliminar_paciente(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        if not cedula:
            return JsonResponse({'error': 'Cédula no proporcionada.'}, status=400)
        try:
            paciente = Pacientes.objects.get(cedula=cedula)
            # Eliminar citas relacionadas primero
            Cita.objects.filter(id_paciente=paciente).delete()
            # Luego eliminar el paciente
            paciente.delete()
            return JsonResponse({'success': True})
        except Pacientes.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado.'}, status=404)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

def programar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/citas/programar/')  # Redirige a una página de éxito
    else:
        form = CitaForm()
    return render(request, 'programar_cita.html', {'form': form})


def generar_password_temporal(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def restablecer_view(request):
    if request.method == 'POST':
        reset_email = request.POST.get('resetEmail')
        try:
            user = User.objects.get(email=reset_email)
            nueva_contraseña = generar_password_temporal()
            user.password = make_password(nueva_contraseña)
            user.save()

            mensaje = (
                f"Hola {user.get_full_name()},\n\n"
                f"Tus credenciales para iniciar sesión son las siguientes:\n\n"
                f"Usuario: {user.username}\n"
                f"Contraseña: {nueva_contraseña}\n\n"
                "Este mensaje es enviado por el soporte técnico de TribiqueTech."
            )

            try:
                send_mail(
                    'Restablecimiento de Contraseña',
                    mensaje,
                    'adm2024clinica@gmail.com',  # Reemplaza con el correo del remitente
                    [reset_email],
                    fail_silently=False,
                )
                messages.success(request, "Correo de restablecimiento enviado.")
                return redirect('/login')  # Redirigir a la página de login en caso de éxito
            except Exception as e:
                messages.error(request, f"Error enviando correo: {str(e)}")
                return JsonResponse({'success': False, 'message': f"Error enviando correo: {str(e)}"})

        except User.DoesNotExist:
            messages.error(request, "Correo no encontrado.")
            return JsonResponse({'success': False, 'message': "Correo no encontrado."})

    return render(request, 'inicio/reset-password.html')

@csrf_exempt
@require_http_methods(["GET"])
def buscar_cita(request):
    id_cita = request.GET.get('id_cita')
    try:
        cita = Citas.objects.get(id_cita=id_cita)
        data = {
            'success': True,
            'cita': {
                'id': cita.id_cita,
                'usuario': cita.id_usuario.nombre_usuario,  # Convertimos a cadena de texto
                'paciente': f"{cita.id_paciente.nombre} {cita.id_paciente.apellido}",  # Convertimos a cadena de texto
                'fecha': cita.fecha_cita.strftime('%Y-%m-%d'),  # Formateamos la fecha
                'hora': cita.hora_cita.strftime('%H:%M:%S'),  # Formateamos la hora
                'estado': cita.estado,
            }
        }
    except Citas.DoesNotExist:
        data = {'success': False}

    return JsonResponse(data)
