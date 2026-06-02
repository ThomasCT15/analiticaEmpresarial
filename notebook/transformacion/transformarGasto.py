def transformar_gastos(df_gastos_limpio):

    #Filtrar los gastos con monto mayor a 50000 agrupados por descripcion (Barras)
    filtro1=df_gastos_limpio.query("monto > 50000")
    agrupacion1=filtro1.groupby("descripcion")["id"].count().reset_index()
    agrupacion1.columns=["descripcion","cantidad"]

    #Todos los gastos agrupados por fecha (Lineas) (sumar)
    filtro2=df_gastos_limpio.query("fecha == fecha")
    agrupacion2=filtro2.groupby("fecha")["monto"].sum().reset_index()
    agrupacion2.columns=["fecha","total"]

    #Todos los gastos agrupados por descripcion (Torta) (sumar)
    filtro3=df_gastos_limpio.query("descripcion == descripcion")
    agrupacion3=filtro3.groupby("descripcion")["monto"].sum().reset_index()
    agrupacion3.columns=["descripcion","total"]

    #Gastos menores a 100000 agrupados por descripcion (Barras) (promedio)
    filtro4=df_gastos_limpio.query("monto < 100000")
    agrupacion4=filtro4.groupby("descripcion")["monto"].mean().reset_index()
    agrupacion4.columns=["descripcion","promedio"]

    #Gastos con monto entre 1000 y 20000 agrupados por fecha (Lineas) (contar)
    filtro5=df_gastos_limpio.query("monto >= 1000 and monto <= 20000")
    agrupacion5=filtro5.groupby("fecha")["id"].count().reset_index()
    agrupacion5.columns=["fecha","cantidad"]

    agrupaciones={
        "agrupacion1":agrupacion1,
        "agrupacion2":agrupacion2,
        "agrupacion3":agrupacion3,
        "agrupacion4":agrupacion4,
        "agrupacion5":agrupacion5
    }

#Todos los gastos agrupados por descripcion (Torta) (sumar)

#Gastos menores a 100000 agrupados por descripcion (Barras) (promedio)

#Gastos con monto entre 1000 y 20000 agrupados por fecha (Lineas) (contar)