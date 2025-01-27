create database clientesbd;
use clientesbd;

creaTe table usuarios(
id int auto_increment primary key not null,
nombres varchar (50),
apellidos varchar (50),
sexo varchar (20)
);

insert into usuarios values (null,"David","Escamilla","Masculino");

select * from usuarios;

UPDATE usuarios SET usuarios.nombres = 'Alberto',usuarios.apellidos = 'Gonzalez',usuarios.sexo = 'Masculino'where usuarios.id=2;

DELETE from usuarios WHERE usuarios.id=5;