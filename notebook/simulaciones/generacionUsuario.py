#Rutina para generar multiples fuentes de datos de un set simulado

import pandas as pd

def convertir_lista_a_fuentes_usuarios(lista_datos):

    data_frame_datos=pd.DataFrame(lista_datos)

    data_frame_datos.to_json(
        "usuarios.json",
        orient="records", #registros de datos en formato JSON
        indent=4 #formato legible con indentación
    )

    data_frame_datos.to_csv(
        "usuarios.csv",
        index=False #no incluir el índice en el archivo CSV
    )

    '''data_frame_datos.to_excel(
        "usuarios.xlsx",
        index=False #no incluir el índice en el archivo Excel
    )'''