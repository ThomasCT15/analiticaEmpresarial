import pandas as pd

def transformar_usuarios(df_usuarios_limpio):

    #Rutina para seleccionar datos de interes y agruparlos para presentar informacion

    #Usuarios mayores de 25 años agrupados por nombres (Grafica de barras) (contar)
    filtro1=df_usuarios_limpio.query("edad > 25")
    agrupacion1=filtro1.groupby("nombres")["id"].count().reset_index()
    agrupacion1.columns=["nombres","cantidad"]

    #Usuarios entre 19 y 30 años agrupados por edad (Grafica de lineas) (contar)
    filtro2=df_usuarios_limpio.query("edad >= 19 and edad <= 30")
    agrupacion2=filtro2.groupby("edad")["id"].count().reset_index()
    agrupacion2.columns=["edad","cantidad"]

    #Todos los usuarios agrupados por correo (Torta) (contar)
    filtro3=df_usuarios_limpio.query("correo == correo")
    agrupacion3=filtro3.groupby("correo")["id"].count().reset_index()
    agrupacion3.columns=["correo","cantidad"]

    #Todos los usuarios que contienen la palabra admin en su contraseña agrupados por nombres (Barras) (contar)
    filtro4=df_usuarios_limpio.query("contraseña.str.contains('admin')")
    agrupacion4=filtro4.groupby("nombres")["id"].count().reset_index()
    agrupacion4.columns=["nombres","cantidad"]

    #Usuarios menores de 40 años agrupados por nombre y edad (torta) (promedio)
    filtro5=df_usuarios_limpio.query("edad < 40")
    agrupacion5=filtro5.groupby("nombres")["edad"].mean().reset_index()
    agrupacion5.columns=["nombres","edad_promedio"]

    agrupaciones={
        "agrupacion1":agrupacion1,
        "agrupacion2":agrupacion2,
        "agrupacion3":agrupacion3,
        "agrupacion4":agrupacion4,
        "agrupacion5":agrupacion5
    }