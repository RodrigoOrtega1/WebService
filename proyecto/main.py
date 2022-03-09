from csv_converter import to_dic
from api_call import peticion

origin = to_dic("dataset1.csv", 2, 3)
del origin['origin_latitude']
# print(len(origin))
print(origin)

destination = to_dic("dataset1.csv", 4, 5)
del destination['destination_latitude']
# print(len(destination))
print(destination)

for x,y in origin.items():
     r = peticion(x,y)
     print(r)
