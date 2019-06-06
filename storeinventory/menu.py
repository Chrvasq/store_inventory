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
            self.get_menu_input()
    
    def get_view_product_input(self):
        try:
            user_input = input('Please enter in a product ID: ')
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
            self.get_view_product_input()

    def main(self):
        pass
