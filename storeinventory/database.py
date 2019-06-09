from .product import Product, db
from .etl import transform_data, load_data
from datetime import date
import csv


class Database:
    @classmethod
    def connect_db_and_load_data(cls):
        """Connects to database, creates tables and loads data from csv"""
        db.connect()
        db.create_tables([Product], safe=True)
        load_data(transform_data('./inventory.csv'))

    @classmethod
    def close_db_connection(cls):
        """Closes connection to database"""
        db.close()

    @classmethod
    def view_product(cls, product_id):
        """Prints out product information to user

        Arguments:
            product_id {int} -- product_id user inputs
        """
        product = Product.get_by_id(product_id)
        print(f'Product ID: {product.product_id}')
        print(f'Product Name: {product.product_name}')
        print(f'Quantity: {product.product_quantity}')
        print(f'Price: ${product.product_price / 100:.2f}\n')

    @classmethod
    def add_product(cls, product_name, price, quantity):
        """Adds a new product to the database based on user input. Conflict
        handling will check if the product name already exists. If it
        already exists, the price, quantity and date_updated values will update
        the existing product.

        Arguments:
            product_name {str} -- product name user inputs
            price {int} -- product price user inputs
            quantity {int} -- product quantity user inputs
        """
        Product.insert(product_name=product_name,
                       product_price=price,
                       product_quantity=quantity,
                       date_updated=date.today()).on_conflict(
                           conflict_target=[Product.product_name],
                           preserve=[Product.product_price,
                                     Product.product_quantity,
                                     Product.date_updated]).execute()
        print(f'\nProduct added successfully!')
        print(f'Product: {product_name} ' +
              f'Price: ${int(price) / 100:.2f} ' +
              f'Quantity: {quantity}\n')

    @classmethod
    def backup_database(cls):
        """Writes database values with header to a csv file"""
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
        print('Database backup complete! File was saved as "db_backup.csv".\n')
