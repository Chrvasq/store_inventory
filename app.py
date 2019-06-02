#!/usr/bin/env python3

from peewee import *

import csv
from datetime import date

db = SqliteDatabase('inventory.db')


def extract_data(csv_file):
    # extract data
    with open(csv_file, newline='') as csvfile:
        inventory = csv.reader(csvfile, delimiter=',')
        rows = list(inventory)
        header = rows[0]
        product_data = rows[1:]
    return header, product_data

def clean_data(csv_file):
    _, product_data = extract_data(csv_file)
    # clean data
    for product in product_data:
        product[1] = int(product[1].lstrip('$').replace('.', ''))
        product[2] = int(product[2])
        last_updated = product[3].split('/')
        product[3] = date(int(last_updated[2]),
                          int(last_updated[0]),
                          int(last_updated[1]))
    return product_data

data = clean_data('inventory.csv')
print(data)
# transform data
# with open('clean_inventory.csv', 'w') as csvfile:
#     inventory_writer = csv.DictWriter(csvfile, fieldnames=header)
#     inventory_writer.writeheader()
#     for product in product_data:
#         inventory_writer.writerow({header[0]: product[0],
#                                    header[1]: int(product[1]),
#                                    header[2]: int(product[2]),
#                                    header[3]: product[3]})