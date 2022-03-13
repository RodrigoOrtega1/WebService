import pandas as pd

def a_df(doc):
    '''
    Toma un archivo .csv
    Regresa un DataFrame
    :param doc: Nombre del documento csv
    :return: Un DataFrame de doc
    '''
    if type(doc) is not str:
        raise ValueError("El nombre del documento debe ser una cadena")
    if ".csv" not in doc:
        raise ValueError("El archivo debe ser de tipo .csv")
    return pd.read_csv(doc)
