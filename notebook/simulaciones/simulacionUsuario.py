#Rutina para simular la  fuente de datos que almacena datos de los usuarios
import random

def simular_usuarios(numeroUsuariosASimular):
    #id
    #nombres
    #contraseña
    #edad
    #correo

    #1. PARA SIMULAR DATOS CON PYTHON
    #CFREO UNAS SEMILLAS DE LOS DATOS A SIMULAR (TEXTO/NUMERO)
    nombres =["Pedro Perez","Maria Gomez","Juan Rodriguez","Ana Martinez","Luis Sanchez","Carla Fernandez","Diego Ramirez","Sofia Lopez","Carlos Gonzalez","Laura Torres"]

    contraseñas = ["admin123","admin987","user123","user987","person123","person987","gap123","gap987","test123","test987"]

    edades = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

    correos = ["pp@correo.com","mg@correo.com","jr@correo.com","am@correo.com","ls@correo.com","cf@correo.com","dr@correo.com","sl@correo.com","cg@correo.com","lt@correo.com"]

    #2. CONSTRUIR UN CICLO PARA GENERAR TANTAS SIMULACIONES COMO EL USUARIO FINAL PIDA
    simulaciones_usuario=[]
    for i in range(numeroUsuariosASimular):
        usuario_simulado={
            "id":random.randint(1,500),
            "nombre":random.choice(nombres),
            "contraseña":random.choice(contraseñas),
            "edad":random.choice(edades),
            "correo":random.choice(correos)
        }

        #Inyectar errorres controlados en el set de datos
        #(SE HACE PARA  QUE LA RUTINA DE SIMULACION SEA LO MAS PARECIDO CON LA REALIDAD)
        probabilidadError= random.random() #Genera un numero aleatorio entre 0 y 1
        if probabilidadError < 0.2: #20% de probabilidad de error
            usuario_simulado["id"]=None #Inyectar un ID invalido
        elif probabilidadError < 0.4: #40% de probabilidad de error
            usuario_simulado["nombres"]=random.choice([None,"11","-10"])
        elif probabilidadError < 0.5: #50% de probabilidad de error
            usuario_simulado["contraseña"]=random.choice([None,"as","-"])
        elif probabilidadError < 0.7: #70% de probabilidad de error
            usuario_simulado["edad"]=random.choice([None,800,-10])
        elif probabilidadError < 0.9: #90% de probabilidad de error
            usuario_simulado["correo"]=" "+usuario_simulado["correo"]+" ".upper() #Inyectar espacios en el correo


        simulaciones_usuario.append(usuario_simulado)
    return simulaciones_usuario
