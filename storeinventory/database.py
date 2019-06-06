from .product import Product, db
from .etl import transform_data, load_data
from datetime import date
import csv


class Database:
    @classmethod
    def connect_db_and_load_data(self):
        db.connect()
        db.create_tables([Product], safe=True)
        load_data(transform_data('./inventory.csv'))

    @classmethod
    def view_product(cls, product_id):
        product = Product.get_by_id(product_id)
        print(f'Product ID: {product.product_id}')
        print(f'Product Name: {product.product_name}')
        print(f'Quantity: {product.product_quantity}')
        print(f'Price: ${product.product_price / 100:.2f}\n')
    
    @classmethod
    def add_product(cls, product_name, price, quantity):
        Product.insert(product_name=product_name,
                       product_price=price,
                       product_quantity=quantity,
                       date_updated=date.today()).on_conflict(
                           conflict_target=[Product.product_name],
                           preserve=[Product.product_price,
                                     Product.product_quantity,
                                     Product.date_updated]).execute()
    @classmethod
    def delete_product(self):
        # TODO
        pass

    @classmethod
    def backup_database(cls):
        with open('db_backup.csv', 'w', newline='') as csvfile:
            fieldnames = ['product_name',
                          'product_price',
                          'product_quantity',
                          'date_updated']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product in Product.select().dicts():
                writer.writerow(
                    {'product_name': product['product_name'],
                     'product_price': product['product_price'],
                     'product_quantity': product['product_quantity'],
                     'date_updated': product['date_updated']})
