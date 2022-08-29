DROP DATABASE IF EXISTS cuidado_en_casa;
CREATE DATABASE IF NOT EXISTS cuidado_en_casa;

USE cuidado_en_casa;

CREATE TABLE personal_medico(
id_medico INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nombre VARCHAR(15),
apellido VARCHAR(15),
telefono VARCHAR(20),
usuario VARCHAR(10),
contrasena VARCHAR(15)
);

INSERT INTO personal_medico(nombre, apellido, telefono, usuario, contrasena)
VALUES ("Jose", "Molina", "+57-3157267890", "josemol", "j0s3m0l"),
("Pedro", "Perez", "+57-3117263452", "pedrope", "p3dr0p3"),
("Monica", "Rangel", "+57-3127223417", "moniran", "m0n1r4n");

CREATE TABLE familiar(
id_familiar INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nombre VARCHAR(15),
apellido VARCHAR(15),
telefono VARCHAR(20),
parentesco VARCHAR(15),
usuario VARCHAR(10),
contrasena VARCHAR(15)
);

INSERT INTO familiar(nombre, apellido, telefono, parentesco, usuario, contrasena)
VALUES ("Juan", "Tupido", "+57-3158977890", "hermano", "juantup", "ju4nt8p"),
("Eliana", "Santoyo", "+57-31172656782", "esposa", "elisan", "3l1s4n");

CREATE TABLE paciente(
id_paciente INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nombre VARCHAR(15),
apellido VARCHAR(15),
edad INT,
telefono VARCHAR(20),
georeferencia VARCHAR(50),
usuario VARCHAR(10),
contrasena VARCHAR(15),
id_medico INT,
id_familiar INT,

FOREIGN KEY (id_medico) REFERENCES personal_medico (id_medico),
FOREIGN KEY (id_familiar) REFERENCES familiar (id_familiar)

);

INSERT INTO paciente(nombre, apellido, edad, telefono, georeferencia, usuario, contrasena, id_medico, id_familiar)
VALUES ("Melkiades", "Tupido", 78, "+57-3247658976", "lat35 - 35", "melktup", "m3lt8p", 1, 1);




CREATE TABLE historial_muestras(
id_muestra INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
id_paciente INT,
fecha TIMESTAMP,
FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)

);

INSERT INTO historial_muestras(id_paciente,fecha)
VALUES (1, '2022-08-20 14:35:00');


CREATE TABLE signos_vitales(

id_signos INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
id_muestra INT,
oximetria VARCHAR(5),
frec_resp VARCHAR(5),
frec_card VARCHAR(5),
temperatura FLOAT,
pres_arterial VARCHAR(5),
glicemia VARCHAR(5),
FOREIGN KEY (id_muestra) REFERENCES historial_muestras (id_muestra)

);

INSERT INTO signos_vitales(id_muestra, oximetria, frec_resp, frec_card, temperatura, pres_arterial, glicemia)
VALUES (1, "90", "90", "90", 36.5, "60", "200");

CREATE TABLE historial_tratamiento(
id_hist_tratamiento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
id_paciente INT,
fecha TIMESTAMP,
FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)

);

INSERT INTO historial_tratamiento(id_paciente,fecha)
VALUES (1, '2022-08-20 14:40:00');



CREATE TABLE tratamiento(

id_tratamiento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
id_hist_tratamiento INT,
tratamiento TEXT(500),
FOREIGN KEY (id_hist_tratamiento) REFERENCES historial_tratamiento (id_hist_tratamiento)

);

INSERT INTO tratamiento(id_hist_tratamiento,tratamiento)
VALUES (1, "100 mg de oxitomatrozina, con un diluiod de 100ml de suero fisio");