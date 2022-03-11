import pandas as pd

def to_df(doc_name):
    """
    Convierte un csv a un DataFrame
    Params:
        doc_name    - Nombre del documento csv
    Returns:
        df          - Un DataFrame del documento dado
    """
    df = pd.read_csv(doc_name)
    return df
