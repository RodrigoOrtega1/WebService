import pandas as pd

def a_df(doc):
    '''
    Toma un archivo .csv
    Regresa un DataFrame
    :param doc: Nombre del documento csv
    :return: Un DataFrame de doc
    '''
    return pd.read_csv(doc)
