from .database import Database
from datetime import date
from .product import Product


class Menu:
    def __init__(self):
        self.menu_options = {'v': 'View product by product_id',
                             'a': 'Add a product to the inventory database',
                             'b': 'Backup database to a .CSV file'}

    def display_menu(self):
        for key, value in self.menu_options.items():
            print(f'{key}) {value}')

    def get_menu_input(self):
        try:
            user_input = input('Please enter v/a/b: ')
            if user_input not in self.menu_options:
                raise ValueError
            else:
                return user_input
        except ValueError:
            print('Invalid choice. Please enter v/a/b.')
            return self.get_menu_input()
    
    def get_view_product_input(self):
        try:
            user_input = input('Please enter in a product ID: ')
            if user_input.isspace():
                raise ValueError(
                    'You didn\'t enter anything. Please enter a number')
            if len(user_input) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a number')
            if user_input.isalpha():
                raise ValueError(
                    'You didn\'t enter a number. Please enter a number.')
            # Check for product id membership
            if int(user_input) not in [
                product.product_id for product in Product.select()]:
                    raise ValueError('Product ID not found.')
            else:
                Database.view_product(user_input)
        except ValueError as error:
            print(error)
            return self.get_view_product_input()
    
    def get_product_input(self):
        product_name = self.get_product_name()
        price = self.get_product_price()
        quantity = self.get_product_quantity()

        Database.add_product(product_name, price, quantity)

    def get_product_name(self):
        try:
            product_name = input('Please enter a product name: ')
            if product_name.isspace():
                raise ValueError(
                    'You didn\'t enter anything. Please enter a product name.')
            if len(product_name) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a product name.')
            else:
                return product_name
        except ValueError as error:
            print(error)
            return self.get_product_name()

    def get_product_quantity(self):
        try:
            quantity = input('Please enter in a quantity: ')
            if quantity.isspace():
                raise ValueError(
                    'You didn\'t enter anything. Please enter a quantity.')
            if len(quantity) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a quantity.')
            if quantity.isalpha():
                raise ValueError(
                    'You didn\'t enter a number. Please enter a number.')
            else:
                return int(quantity)
        except ValueError as error:
            print(error)
            return self.get_product_quantity()

    def get_product_price(self):
        try:
            price = input('Please enter in a price: ')
            if price.isspace():
                raise ValueError(
                    'You didn\'t enter anything. Please enter a price.')
            if len(price) == 0:
                raise ValueError(
                    'You didn\'t enter anything. Please enter a price.')
            if price.isalpha():
                raise ValueError(
                    'You didn\'t enter a number. Please enter a number.')
            else:
                return int(float(price.lstrip('$')) * 100)

        except ValueError as error:
            print(error)
            return self.get_product_price()

    def main(self):
        pass
