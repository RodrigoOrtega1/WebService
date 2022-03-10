import csv
import pandas as pd

# Clase que implementa un convertidor de archivo csv a DataFrame de python

# Convierte un csv a DataFrame de la libreria 'pandas'
def to_df(doc_name):
    df = pd.read_csv(doc_name)
    return df

# Convierte un documento csv a diccionario de python
def to_dic(doc_name, row1, row2):
    dic = {}
    with open(doc_name, mode = 'r') as inp:
        reader = csv.reader(inp)
        dic = {rows[row1]:rows[row2] for rows in reader}
    return dic
