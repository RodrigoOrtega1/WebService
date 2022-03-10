import pandas as pd

# Clase que implementa un convertidor de archivo csv a DataFrame de python

# Convierte un csv a DataFrame de la libreria 'pandas'
def to_df(doc_name):
    df = pd.read_csv(doc_name)
    return df
