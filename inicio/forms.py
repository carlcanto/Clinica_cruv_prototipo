from django import forms
from historial.models import Pacientes, Citas

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'