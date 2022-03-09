import csv

def to_dic(doc_name, row1, row2):
    dic = {}
    with open(doc_name, mode = 'r') as inp:
        reader = csv.reader(inp)
        dic = {rows[row1]:rows[row2] for rows in reader}
    return dic

# origin = to_dic("dataset1.csv", 2, 3)
# del origin['origin_latitude']
# print(len(origin))
# print(origin)
#
# destination = to_dic("dataset1.csv", 4, 5)
# del destination['destination_latitude']
# print(len(destination))
# print(destination)
