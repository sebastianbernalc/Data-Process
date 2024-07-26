import pandas as pd
from Proceso import tools, dictionary
import matplotlib.pyplot as plt

def proceso():
    df = pd.read_csv('./DataSets/dataset_1.csv', index_col=0)
    df_clean = (
        df.pipe(tools.remove_negative_values, 'Edad')
        .pipe(tools.remove_negative_values, 'Ingresos')
        .pipe(tools.remove_negative_values, 'Hijos')
        .pipe(tools.remove_outliers, 'Edad')
        .pipe(tools.remove_outliers, 'Ingresos')
        .pipe(tools.remove_outliers, 'Hijos')
        .pipe(tools.map_column_values, 'Nivel_Educación', dictionary.get_mapping('education'))
        .pipe(tools.map_column_values, 'Género', dictionary.get_mapping('gender'))
        .pipe(tools.fill_na_value, 'Ciudad', 'No especificado')
        .pipe(tools.fill_na_value, 'Género', 'No especificado')
        .pipe(tools.fill_na_value, 'Nivel_Educación', 'No especificado')
        .pipe(tools.fill_na_value, 'Edad', df['Edad'].median())
        .pipe(tools.fill_na_value, 'Hijos', df['Hijos'].median())
        .pipe(tools.fill_na_value, 'Ingresos', df['Ingresos'].mean())
        .pipe(tools.fill_na_value, 'Altura', df['Altura'].mean())
    )
    df_clean.to_excel('./DataSets/dataset_1_clean.xlsx', index=False)

    return df_clean







