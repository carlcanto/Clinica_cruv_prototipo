CREATE DATABASE IF NOT EXISTS clinica_cruv;
USE clinica_cruv;

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo_electronico VARCHAR(100),
    contraseña VARCHAR(100),
    tipo_usuario ENUM('administrador', 'usuario normal'),
    nombre_usuario VARCHAR(50) -- Nuevo campo añadido
);

CREATE TABLE Pacientes (
  id_paciente INT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  fecha_nacimiento DATE,
  direccion VARCHAR(100),
  telefono VARCHAR(20),
  cedula VARCHAR(20),
  seguro_social VARCHAR(20),
  edad INT,
  sexo ENUM('M', 'F'),
  lugar_de_trabajo VARCHAR(100),
  ocupacion VARCHAR(50),
  direccion_trabajo VARCHAR(100),
  telefono_trabajo VARCHAR(20),
  persona_emergencia VARCHAR(100),
  telefono_emergencia VARCHAR(20),
  direccion_emergencia VARCHAR(100),
  relacion_emergencia VARCHAR(50)
);

CREATE TABLE Consultorios (
  id_consultorio INT PRIMARY KEY,
  nombre VARCHAR(50),
  ubicacion VARCHAR(100),
  disponible ENUM('si', 'no')
);

CREATE TABLE Citas (
  id_cita INT PRIMARY KEY,
  id_usuario INT,
  id_paciente INT,
  fecha_cita DATE,
  hora_cita TIME,
  estado ENUM('programada', 'anulada', 'transferida', 'reasignada'),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Expedientes (
  id_expediente INT PRIMARY KEY,
  id_paciente INT,
  fecha_apertura DATE,
  fecha_cierre DATE,
  estado ENUM('abierto', 'cerrado'),
  observaciones TEXT,
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Reportes (
  id_reporte INT PRIMARY KEY,
  id_usuario INT,
  tipo_reporte VARCHAR(50),
  fecha_generacion DATE,
  archivo_adjunto BLOB,
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE historial_medico (
  id_historial INT PRIMARY KEY AUTO_INCREMENT,
  id_paciente INT,
  antecedentes_familiares_diabetes ENUM('Si', 'No'),
  antecedentes_familiares_corazon ENUM('Si', 'No'),
  antecedentes_familiares_presion_alta ENUM('Si', 'No'),
  antecedentes_familiares_tratamiento_psiquiatrico ENUM('Si', 'No'),
  antecedentes_familiares_cancer ENUM('Si', 'No'),
  antecedentes_familiares_convulsiones ENUM('Si', 'No'),
  antecedentes_familiares_anemia_falciforme ENUM('Si', 'No'),
  antecedentes_familiares_trastorno_coagulacion ENUM('Si', 'No'),
  antecedentes_familiares_vihsida ENUM('Si', 'No'),
  antecedentes_familiares_otras ENUM('Si', 'No'),
  antecedentes_familiares_descripcion VARCHAR(100),
  antecedentes_personales_diabetes ENUM('Si', 'No'),
  antecedentes_personales_corazon ENUM('Si', 'No'),
  antecedentes_personales_presion_alta ENUM('Si', 'No'),
  antecedentes_personales_tratamiento_psiquiatrico ENUM('Si', 'No'),
  antecedentes_personales_cancer ENUM('Si', 'No'),
  antecedentes_personales_anemia ENUM('Si', 'No'),
  antecedentes_personales_trastorno_coagulacion ENUM('Si', 'No'),
  antecedentes_personales_alergias ENUM('Si', 'No'),
  antecedentes_personales_alergias_descripcion VARCHAR(100),
  antecedentes_personales_infeccion_sexual ENUM('Si', 'No'),
  antecedentes_personales_problemas_digestivos ENUM('Si', 'No'),
  antecedentes_personales_hepatitis ENUM('Si', 'No'),
  antecedentes_personales_vihsida ENUM('Si', 'No'),
  antecedentes_personales_embarazo ENUM('Si', 'No'),
  antecedentes_personales_otras ENUM('Si', 'No'),
  antecedentes_personales_descripcion VARCHAR(100),
  toma_medicamentos ENUM('Si', 'No'),
  medicamentos_descripcion VARCHAR(100),
  toma_drogas ENUM('Si', 'No'),
  drogas_descripcion VARCHAR(100),
  toma_medicamentos_naturales ENUM('Si', 'No'),
  medicamentos_naturales_descripcion VARCHAR(100),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Historial_Bucal (
  id_historial_bucal INT PRIMARY KEY AUTO_INCREMENT,
  id_paciente INT,
  ha_recibido_anestesia ENUM('Si', 'No'),
  sensibilidad_dental ENUM('No', 'Calor', 'Dulce', 'Frío', 'Masticación'),
  hallazgos TEXT,
  diagnostico TEXT,
  pronostico TEXT,
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Hallazgos_dentofaciales (
  id_hallazgos_dentofaciales INT PRIMARY KEY AUTO_INCREMENT,
  id_paciente INT,
  habitos TEXT,
  clasificacion_molar VARCHAR(50),
  ATM ENUM('Normal', 'Anormal'),
  dolor ENUM('Si', 'No'),
  desviacion ENUM('Si', 'No'),
  ruidos ENUM('Si', 'No'),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Hallazgos_tejidos_blandos (
  id_hallazgos_tejidos_blandos INT PRIMARY KEY AUTO_INCREMENT,
  id_paciente INT,
  ganglios ENUM('Normal', 'Anormal'),
  glandulas_salivares ENUM('Normal', 'Anormal'),
  mucosa_bucal ENUM('Normal', 'Anormal'),
  labios ENUM('Normal', 'Anormal'),
  lengua ENUM('Normal', 'Anormal'),
  paladar_duro ENUM('Normal', 'Anormal'),
  paladar_blando ENUM('Normal', 'Anormal'),
  rebordes ENUM('Normal', 'Anormal'),
  bucofaringe ENUM('Normal', 'Anormal'),
  encias ENUM('Normal', 'Anormal'),
  piso_boca ENUM('Normal', 'Anormal'),
  carrillos ENUM('Normal', 'Anormal'),
  medico_atiende VARCHAR(100),
  secuencia_tratamiento TEXT,
  numero_citas INT,
  costo_total DECIMAL(10, 2),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Plan_tratamiento (
  id_plan INT PRIMARY KEY AUTO_INCREMENT,
  id_paciente INT,
  fecha_inicio DATE,
  numero_citas INT,
  costo_total DECIMAL(10, 2),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

ALTER TABLE Consultorios
ADD COLUMN id_cita INT,
ADD CONSTRAINT fk_consultorio_citas FOREIGN KEY (id_cita) REFERENCES Citas(id_cita);

ALTER TABLE Citas
ADD CONSTRAINT fk_usuario_cita
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario);

ALTER TABLE Citas
ADD CONSTRAINT fk_paciente_cita
FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente);

ALTER TABLE Expedientes
ADD CONSTRAINT fk_paciente_expediente
FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente);

ALTER TABLE Reportes
ADD CONSTRAINT fk_usuario_reporte
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario);