from api_call import peticion
from csv_converter import to_dic

origin = to_dic("dataset1.csv", 2, 3)
del origin['origin_latitude']
destination = to_dic("dataset1.csv", 4, 5)
del destination['destination_latitude']
