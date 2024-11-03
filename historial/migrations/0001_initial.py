# Generated by Django 5.0.7 on 2024-07-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id_cita', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_cita', models.DateField(blank=True, null=True)),
                ('hora_cita', models.TimeField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consultorios',
            fields=[
                ('id_consultorio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=100, null=True)),
                ('disponible', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'consultorios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Expedientes',
            fields=[
                ('id_expediente', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_apertura', models.DateField(blank=True, null=True)),
                ('fecha_cierre', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=7, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'expedientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HallazgosDentofaciales',
            fields=[
                ('id_hallazgos_dentofaciales', models.AutoField(primary_key=True, serialize=False)),
                ('habitos', models.TextField(blank=True, null=True)),
                ('clasificacion_molar', models.CharField(blank=True, max_length=50, null=True)),
                ('atm', models.CharField(blank=True, db_column='ATM', max_length=7, null=True)),
                ('dolor', models.CharField(blank=True, max_length=2, null=True)),
                ('desviacion', models.CharField(blank=True, max_length=2, null=True)),
                ('ruidos', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'hallazgos_dentofaciales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HallazgosTejidosBlandos',
            fields=[
                ('id_hallazgos_tejidos_blandos', models.AutoField(primary_key=True, serialize=False)),
                ('ganglios', models.CharField(blank=True, max_length=7, null=True)),
                ('glandulas_salivares', models.CharField(blank=True, max_length=7, null=True)),
                ('mucosa_bucal', models.CharField(blank=True, max_length=7, null=True)),
                ('labios', models.CharField(blank=True, max_length=7, null=True)),
                ('lengua', models.CharField(blank=True, max_length=7, null=True)),
                ('paladar_duro', models.CharField(blank=True, max_length=7, null=True)),
                ('paladar_blando', models.CharField(blank=True, max_length=7, null=True)),
                ('rebordes', models.CharField(blank=True, max_length=7, null=True)),
                ('bucofaringe', models.CharField(blank=True, max_length=7, null=True)),
                ('encias', models.CharField(blank=True, max_length=7, null=True)),
                ('piso_boca', models.CharField(blank=True, max_length=7, null=True)),
                ('carrillos', models.CharField(blank=True, max_length=7, null=True)),
                ('medico_atiende', models.CharField(blank=True, max_length=100, null=True)),
                ('secuencia_tratamiento', models.TextField(blank=True, null=True)),
                ('numero_citas', models.IntegerField(blank=True, null=True)),
                ('costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'hallazgos_tejidos_blandos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialBucal',
            fields=[
                ('id_historial_bucal', models.AutoField(primary_key=True, serialize=False)),
                ('ha_recibido_anestesia', models.CharField(blank=True, max_length=2, null=True)),
                ('sensibilidad_dental', models.CharField(blank=True, max_length=11, null=True)),
                ('hallazgos', models.TextField(blank=True, null=True)),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('pronostico', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historial_bucal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('antecedentes_familiares_diabetes', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_corazon', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_presion_alta', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_tratamiento_psiquiatrico', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_cancer', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_convulsiones', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_anemia_falciforme', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_trastorno_coagulacion', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_vihsida', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_otras', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_familiares_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('antecedentes_personales_diabetes', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_corazon', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_presion_alta', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_tratamiento_psiquiatrico', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_cancer', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_anemia', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_trastorno_coagulacion', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_alergias', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_alergias_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('antecedentes_personales_infeccion_sexual', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_problemas_digestivos', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_hepatitis', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_vihsida', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_embarazo', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_otras', models.CharField(blank=True, max_length=2, null=True)),
                ('antecedentes_personales_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('toma_medicamentos', models.CharField(blank=True, max_length=2, null=True)),
                ('medicamentos_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('toma_drogas', models.CharField(blank=True, max_length=2, null=True)),
                ('drogas_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('toma_medicamentos_naturales', models.CharField(blank=True, max_length=2, null=True)),
                ('medicamentos_naturales_descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'historial_medico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('cedula', models.CharField(blank=True, max_length=20, null=True)),
                ('seguro_social', models.CharField(blank=True, max_length=20, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('lugar_de_trabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_trabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_trabajo', models.CharField(blank=True, max_length=20, null=True)),
                ('persona_emergencia', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_emergencia', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_emergencia', models.CharField(blank=True, max_length=100, null=True)),
                ('relacion_emergencia', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pacientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanTratamiento',
            fields=[
                ('id_plan', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('numero_citas', models.IntegerField(blank=True, null=True)),
                ('costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'plan_tratamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id_reporte', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_reporte', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_generacion', models.DateField(blank=True, null=True)),
                ('archivo_adjunto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reportes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('correo_electronico', models.CharField(blank=True, max_length=100, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_usuario', models.CharField(blank=True, max_length=14, null=True)),
                ('nombre_usuario', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]