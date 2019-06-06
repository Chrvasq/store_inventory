import csv
from .product import Product
from datetime import date


def extract_data(csv_file):
    # read and extract data
    with open(csv_file, newline='') as csvfile:
        inventory = csv.reader(csvfile, delimiter=',')
        rows = list(inventory)
        header = rows[0]
        product_data = rows[1:]
    return header, product_data


def transform_data(csv_file):
    header, product_data = extract_data(csv_file)
    # clean data
    for product in product_data:
        product[1] = int(float(product[1].lstrip('$')) * 100)
        product[2] = int(product[2])
        last_updated = product[3].split('/')
        product[3] = date(int(last_updated[2]),
                          int(last_updated[0]),
                          int(last_updated[1]))
    # transform data to list of dictionary entries for each product
    inventory = []
    for product in product_data:
        inventory.append({header[0]: product[0],
                          header[1]: product[1],
                          header[2]: product[2],
                          header[3]: product[3]})
    return inventory


def load_data(product_list):
    # load data from csv into db
    for product in product_list:
        Product.insert(product_name=product['product_name'],
                       product_price=product['product_price'],
                       product_quantity=product['product_quantity'],
                       date_updated=product['date_updated']).on_conflict(
                           conflict_target=[Product.product_name],
                           preserve=[Product.product_price,
                                     Product.product_quantity,
                                     Product.date_updated]).execute()
