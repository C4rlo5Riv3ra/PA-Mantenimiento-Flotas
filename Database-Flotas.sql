-- PERSONA
CREATE TABLE persona (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    doc_identity VARCHAR(8) UNIQUE,
    telefono VARCHAR(10),
    direccion VARCHAR(80)
);

-- ROL DE USUARIO
CREATE TABLE rol (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE
);

-- ESTADO DE USUARIO
CREATE TABLE estado_usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE
);

-- USUARIO
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    id_persona INT REFERENCES persona(id),
    id_rol INT REFERENCES rol(id),
    id_estado INT REFERENCES estado_usuario(id)
);

-- TIPO DE VEHÍCULO
CREATE TABLE tipo_vehiculo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(30) UNIQUE
);

-- VEHÍCULO
CREATE TABLE vehiculo (
    id SERIAL PRIMARY KEY,
    placa VARCHAR(15) UNIQUE,
    marca VARCHAR(25),
    modelo VARCHAR(20),
    anio INT CHECK (anio >= 1900 AND anio <= EXTRACT(YEAR FROM CURRENT_DATE)),
    id_tipo_vehiculo INT REFERENCES tipo_vehiculo(id),
    estado BOOLEAN DEFAULT TRUE,
    kilometraje_actual FLOAT DEFAULT 0,
    last_date_support DATE,
    next_date_support DATE
);

-- ESTADO DE CONDUCTOR
CREATE TABLE estado_conductor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE
);

-- CONDUCTOR
CREATE TABLE conductor (
    id SERIAL PRIMARY KEY,
    id_persona INT REFERENCES persona(id),
    licence_drive VARCHAR(30),
    fecha_ingreso DATE,
    id_estado INT REFERENCES estado_conductor(id)
);

-- ESTADO DE ASIGNACIÓN
CREATE TABLE estado_asignacion (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE
);

-- ASIGNACIÓN VEHÍCULO - CONDUCTOR
CREATE TABLE asignacion (
    id SERIAL PRIMARY KEY,
    id_vehiculo INT REFERENCES vehiculo(id),
    id_conductor INT REFERENCES conductor(id),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    id_estado INT REFERENCES estado_asignacion(id)
);

-- TIPO DE MANTENIMIENTO
CREATE TABLE tipo_mantenimiento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE
);

-- MANTENIMIENTO
CREATE TABLE mantenimiento (
    id SERIAL PRIMARY KEY,
    id_vehiculo INT REFERENCES vehiculo(id),
    id_tipo_mantenimiento INT REFERENCES tipo_mantenimiento(id),
    descripcion VARCHAR(250),
    fecha DATE,
    kilometraje FLOAT,
    costo FLOAT,
    taller VARCHAR(100)
);

-- SERVICIOS DE MANTENIMIENTO
CREATE TABLE servicio_mantenimiento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

-- DETALLE DE SERVICIOS EN MANTENIMIENTOS
CREATE TABLE detalle_mantenimiento (
    id SERIAL PRIMARY KEY,
    id_mantenimiento INT REFERENCES mantenimiento(id),
    id_servicio INT REFERENCES servicio_mantenimiento(id)
);

-- TIPO DE ALERTA
CREATE TABLE tipo_alerta (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE
);

-- ESTADO DE ALERTA
CREATE TABLE estado_alerta (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE
);

-- ALERTAS POR MANTENIMIENTO
CREATE TABLE alerta_mantenimiento (
    id SERIAL PRIMARY KEY,
    id_vehiculo INT REFERENCES vehiculo(id),
    id_tipo_alerta INT REFERENCES tipo_alerta(id),
    mensaje VARCHAR(250),
    fecha_alerta DATE,
    id_estado INT REFERENCES estado_alerta(id)
);
