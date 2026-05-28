#Limpiamos datos para garantizar que nuestro analisis sea de calidad y confiable
#No analizamos datos que no tienen proposito o que pueden generar ruido en nuestro analisis

#PASOS GENERICOS PARA LIMPIAR DATOS

#1. LIMPIAR LOS TEXTOS

#2. LIMPIAR LOS NUMEROS

#3. LIMPIAR LAS FECHAS Y OTROS FORMATOS

import pandas as pd

def limpiar_datos_usuario(data_frame_datos):

    #1.1 se eliminan los espacios si los hay de los campos de tipo texto
    data_frame_usuarios["nombres"]=data_frame_usuarios["nombres"].astype("string").str.strip().str.lower()
    data_frame_usuarios["contraseña"]=data_frame_usuarios["contraseña"].astype("string").str.strip().str.lower()
    data_frame_usuarios["correo"]=data_frame_usuarios["correo"].astype("string").str.strip().str.lower()
    
       #str.strip() elimina los espacios al inicio y al final del texto
       #str.lower() convierte el texto a minusculas para estandarizarlo

    #1.2 se limpian los valores que no tiene los datos esperados
    valores_esperados_nombres=["Pedro Perez","Maria Gomez","Juan Rodriguez","Ana Martinez","Luis Sanchez","Carla Fernandez","Diego Ramirez","Sofia Lopez","Carlos Gonzalez","Laura Torres"]
    data_frame_usuarios["nombres"]=data_frame_usuarios["nombres"].where(
        data_frame_usuarios["nombres"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_contraseña=["admin123","admin987","user123","user987","person123","person987","gap123","gap987","test123","test987"]
    data_frame_usuarios["contraseña"]=data_frame_usuarios["contraseña"].where(
        data_frame_usuarios["contraseña"].isin(valores_esperados_contraseña),
        pd.NA
    )

    valores_esperados_correos=["pp@correo.com","mg@correo.com","jr@correo.com","am@correo.com","ls@correo.com","cf@correo.com","dr@correo.com","sl@correo.com","cg@correo.com","lt@correo.com"]
    data_frame_usuarios["correo"]=data_frame_usuarios["correo"].where(
        data_frame_usuarios["correo"].isin(valores_esperados_correos),
        pd.NA
    )

    #2.1 si es un numero verifico que de verdad sea un numero
    data_frame_usuarios["id"]=pd.to_numeric(data_frame_usuarios["id"])
    data_frame_usuarios["edad"]=pd.to_numeric(data_frame_usuarios["edad"])

    #2.2 verifico que los valores numericos esten en el rango que me sirven
    data_frame_usuarios["id"]=data_frame_usuarios[data_frame_usuarios["id"]>0]
    data_frame_usuarios["edad"]=data_frame_usuarios[data_frame_usuarios["edad"]<150]
    data_frame_usuarios["edad"]=data_frame_usuarios[data_frame_usuarios["edad"]>0]

    #3.1 si es una fecha, verificar que efectivamente sea una fecha

    #CASO ESPECIAL: ELIMINO los registros cuyos datos sean vacios
    columnas_obligatorias=["id","correo","contraseña"]
    data_frame_usuarios=data_frame_usuarios.dropna(subset=columnas_obligatorias)

    return data_frame_usuarios