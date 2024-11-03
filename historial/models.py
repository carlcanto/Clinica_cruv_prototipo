
from django.db import models

class Citas(models.Model):
    id_cita = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    fecha_cita = models.DateField(blank=True, null=True)
    hora_cita = models.TimeField(blank=True, null=True)
    estado = models.CharField(max_length=11, blank=True, null=True)
    
    def __str__(self):
        return f"Cita {self.id_cita} - {self.id_paciente}"

    class Meta:
        managed = False
        db_table = 'citas'


class Consultorios(models.Model):
    id_consultorio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    disponible = models.CharField(max_length=2, blank=True, null=True)
    id_cita = models.ForeignKey(Citas, models.DO_NOTHING, db_column='id_cita', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultorios'


class Expedientes(models.Model):
    id_expediente = models.IntegerField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    fecha_apertura = models.DateField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=7, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedientes'


class HallazgosDentofaciales(models.Model):
    id_hallazgos_dentofaciales = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    habitos = models.TextField(blank=True, null=True)
    clasificacion_molar = models.CharField(max_length=50, blank=True, null=True)
    atm = models.CharField(db_column='ATM', max_length=7, blank=True, null=True)  # Field name made lowercase.
    dolor = models.CharField(max_length=2, blank=True, null=True)
    desviacion = models.CharField(max_length=2, blank=True, null=True)
    ruidos = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hallazgos_dentofaciales'


class HallazgosTejidosBlandos(models.Model):
    id_hallazgos_tejidos_blandos = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    ganglios = models.CharField(max_length=7, blank=True, null=True)
    glandulas_salivares = models.CharField(max_length=7, blank=True, null=True)
    mucosa_bucal = models.CharField(max_length=7, blank=True, null=True)
    labios = models.CharField(max_length=7, blank=True, null=True)
    lengua = models.CharField(max_length=7, blank=True, null=True)
    paladar_duro = models.CharField(max_length=7, blank=True, null=True)
    paladar_blando = models.CharField(max_length=7, blank=True, null=True)
    rebordes = models.CharField(max_length=7, blank=True, null=True)
    bucofaringe = models.CharField(max_length=7, blank=True, null=True)
    encias = models.CharField(max_length=7, blank=True, null=True)
    piso_boca = models.CharField(max_length=7, blank=True, null=True)
    carrillos = models.CharField(max_length=7, blank=True, null=True)
    medico_atiende = models.CharField(max_length=100, blank=True, null=True)
    secuencia_tratamiento = models.TextField(blank=True, null=True)
    numero_citas = models.IntegerField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hallazgos_tejidos_blandos'


class HistorialBucal(models.Model):
    id_historial_bucal = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    ha_recibido_anestesia = models.CharField(max_length=2, blank=True, null=True)
    sensibilidad_dental = models.CharField(max_length=11, blank=True, null=True)
    hallazgos = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    pronostico = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_bucal'


class HistorialMedico(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    antecedentes_familiares_diabetes = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_corazon = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_presion_alta = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_tratamiento_psiquiatrico = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_cancer = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_convulsiones = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_anemia_falciforme = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_trastorno_coagulacion = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_vihsida = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_otras = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_familiares_descripcion = models.CharField(max_length=100, blank=True, null=True)
    antecedentes_personales_diabetes = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_corazon = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_presion_alta = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_tratamiento_psiquiatrico = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_cancer = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_anemia = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_trastorno_coagulacion = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_alergias = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_alergias_descripcion = models.CharField(max_length=100, blank=True, null=True)
    antecedentes_personales_infeccion_sexual = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_problemas_digestivos = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_hepatitis = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_vihsida = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_embarazo = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_otras = models.CharField(max_length=2, blank=True, null=True)
    antecedentes_personales_descripcion = models.CharField(max_length=100, blank=True, null=True)
    toma_medicamentos = models.CharField(max_length=2, blank=True, null=True)
    medicamentos_descripcion = models.CharField(max_length=100, blank=True, null=True)
    toma_drogas = models.CharField(max_length=2, blank=True, null=True)
    drogas_descripcion = models.CharField(max_length=100, blank=True, null=True)
    toma_medicamentos_naturales = models.CharField(max_length=2, blank=True, null=True)
    medicamentos_naturales_descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_medico'


class Pacientes(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    seguro_social = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    lugar_de_trabajo = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=100, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=20, blank=True, null=True)
    persona_emergencia = models.CharField(max_length=100, blank=True, null=True)
    telefono_emergencia = models.CharField(max_length=20, blank=True, null=True)
    direccion_emergencia = models.CharField(max_length=100, blank=True, null=True)
    relacion_emergencia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes'


class PlanTratamiento(models.Model):
    id_plan = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes, models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    numero_citas = models.IntegerField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_tratamiento'


class Reportes(models.Model):
    id_reporte = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    tipo_reporte = models.CharField(max_length=50, blank=True, null=True)
    fecha_generacion = models.DateField(blank=True, null=True)
    archivo_adjunto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportes'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.CharField(max_length=100, blank=True, null=True)
    contrasena = models.CharField(max_length=100, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=14, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
