import csv
from storeinventory.product import Product, db
from datetime import date

def extract_and_clean_data(csv_file):
    # read and extract data
    with open(csv_file, newline='') as csvfile:
        inventory = csv.reader(csvfile, delimiter=',')
        rows = list(inventory)
        header = rows[0]
        product_data = rows[1:]
    # clean data
    for product in product_data:
        product[1] = int(product[1].lstrip('$').replace('.', ''))
        product[2] = int(product[2])
        last_updated = product[3].split('/')
        product[3] = date(int(last_updated[2]),
                          int(last_updated[0]),
                          int(last_updated[1]))
    return header, product_data


def transform_data(csv_file):
    header, product_data = extract_and_clean_data(csv_file)
    # transform data to list of dictionary entries for each product
    inventory = []
    for product in product_data:
        inventory.append({header[0]: product[0],
                          header[1]: product[1],
                          header[2]: product[2],
                          header[3]: product[3]})
    return inventory

def add_data_from_csv(product_list):
    for product in product_list:
        Product.create(product_name=product['product_name'],
                       product_quantity=product['product_quantity'],
                       product_price=product['product_price'],
                       date_updated=product['date_updated'])
