from .product import Product
from datetime import date
import csv


class Database:
    def __init__(self):
        self.product_name = None
        self.product_quantity = None
        self.product_price = None
    
    def view_product(self, product_id):
        product = Product.get_by_id(product_id)
        print(f'Product Name: {product.product_name}')
        print(f'Quantity: {product.product_quantity}')
        print(f'Price: ${product.product_price / 100:.2f}\n')

    def add_product(self):
        self.get_product_input()

        Product.insert(product_name=self.product_name,
                       product_price=self.product_price,
                       product_quantity=self.product_quantity,
                       date_updated=date.today()).on_conflict(
                           conflict_target=[Product.product_name],
                           preserve=[Product.product_price,
                                     Product.product_quantity,
                                     Product.date_updated]).execute()
    def delete_product(self):
        # TODO
        pass

    def get_product_input(self):
        prompt_user = True
        while prompt_user:
            if not self.product_name:
                self.get_product_name()
            if not self.product_quantity:
                self.get_product_quantity()
            if not self.product_price:
                self.get_product_price()
            else:
                prompt_user = False

    def get_product_name(self):
        try:
            product_name = input('Please enter a product name: ')
            if len(product_name) == 0:
                raise ValueError
            else:
                self.product_name = product_name
        except ValueError:
            print('You didn\'t enter anything. Please enter a product name.')
            self.get_product_name()

    def get_product_quantity(self):
        try:
            quantity = input('Please enter in a quantity: ')
            if len(quantity) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a quantity.')
            if quantity.isalpha():
                raise ValueError(
                    'You didn\'t enter a number. Please enter a number.')
            else:
                self.product_quantity = int(quantity)
        except ValueError as error:
            print(error)
            self.get_product_quantity()

    def get_product_price(self):
        try:
            price = input('Please enter in a price: ')
            if len(price) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a price.')
            if price.isalpha():
                raise ValueError(
                    'You didn\'t enter a number. Please enter a number.')
            else:
                self.product_price = int(float(price.lstrip('$')) * 100)

        except ValueError as error:
            print(error)
            self.get_product_price()
    
    def backup_database(self):
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
