from .database import Database, Product
from os import system, name, sys

YELLOW = '\033[1;93m'  # Bold and yellow
END = '\033[0m'  # Reset formatting


class Menu:
    def __init__(self):
        self.menu_options = {'v': 'View product by product_id',
                             'a': 'Add a product to the inventory database',
                             'b': 'Backup database to a .CSV file',
                             'q': 'Quit'}

    def welcome_message(self):
        welcome_message = ' Store Inventory '
        print('#' * (len(welcome_message) + 2))
        print(f'#{welcome_message}#')
        print('#' * (len(welcome_message) + 2))
        print('\n')

    def clear_screen(self):
        system('cls' if name == 'nt' else 'clear')

    def display_menu(self):
        for key, value in self.menu_options.items():
            print(f'{key}) {value}')
        print('\n')

    def get_menu_input(self):
        try:
            user_input = input('Please enter v/a/b/q: ')
            print('\n')
            if user_input.lower() not in self.menu_options:
                raise ValueError
            else:
                return user_input.lower()
        except ValueError:
            print(YELLOW + 'Invalid choice. Please enter v/a/b/q.\n' + END)
            return self.get_menu_input()

    def get_view_product_input(self):
        try:
            user_input = input('Please enter in a product ID: ')
            print('\n')
            if len(user_input) == 0:
                raise ValueError(
                    YELLOW +
                    'You didn\'t enter anything. Please enter a number.\n' +
                    END)
            if user_input.isspace():
                raise ValueError(
                    YELLOW +
                    'You didn\'t enter anything. Please enter a number.\n' +
                    END)
            if not user_input.isalnum():
                raise ValueError(
                    YELLOW +
                    'You didn\'t enter a number. Please enter a number.\n' +
                    END)
            if user_input.isalpha():
                raise ValueError(
                    YELLOW + 'You didn\'t enter a number. Please enter a '
                    'number.\n' + END)
            # Check for product id membership
            if int(user_input) not in [product.product_id for product
                                       in Product.select()]:
                raise ValueError(YELLOW + 'Product ID not found.\n' + END)
            else:
                self.clear_screen()
                Database.view_product(user_input)
        except ValueError as error:
            print(error)
            return self.get_view_product_input()

    def get_product_input(self):
        product_name = self.get_product_name()
        price = self.get_product_price()
        quantity = self.get_product_quantity()
        return product_name, price, quantity

    def get_product_name(self):
        try:
            product_name = input('Please enter a product name: ')
            print('\n')
            if product_name.isspace():
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'product name.\n' + END)
            if len(product_name) == 0:
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'product name.\n' + END)
            else:
                return product_name
        except ValueError as error:
            print(error)
            return self.get_product_name()

    def get_product_quantity(self):
        try:
            quantity = input('Please enter in a quantity: ')
            print('\n')
            if len(quantity) == 0:
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'quantity.\n' + END)
            if quantity.isspace():
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'quantity.\n' + END)
            if not quantity.isalnum():
                raise ValueError(
                    YELLOW +
                    'You didn\'t enter a number. Please enter a number.\n' +
                    END)
            if quantity.isalpha():
                raise ValueError(
                    YELLOW + 'You didn\'t enter a number. Please enter a '
                    'number.\n' + END)
            else:
                return int(quantity)
        except ValueError as error:
            print(error)
            return self.get_product_quantity()

    def get_product_price(self):
        try:
            price = input('Please enter in a price: ')
            print('\n')
            if len(price) == 0:
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'price.\n' + END)
            if price.isspace():
                raise ValueError(
                    YELLOW + 'You didn\'t enter anything. Please enter a '
                    'price.\n' + END)
            if not price.isalnum() and '.' not in price:
                raise ValueError(
                    YELLOW +
                    'You didn\'t enter a number. Please enter a number.\n' +
                    END)
            if price.isalpha():
                raise ValueError(
                    YELLOW + 'You didn\'t enter a number. Please enter a '
                    'number.\n' + END)
            else:
                return int(float(price.lstrip('$')) * 100)

        except ValueError as error:
            print(error)
            return self.get_product_price()

    def main(self, user_input=None):
        active = True
        if not user_input:  # Run the first time app launches
            Database.connect_db_and_load_data()
            self.clear_screen()
            self.welcome_message()
            self.display_menu()
            user_input = self.get_menu_input()
        while active:
            if user_input == 'v':
                self.get_view_product_input()
                self.display_menu()
                return self.main(self.get_menu_input())
            if user_input == 'a':
                product_name, price, quantity = self.get_product_input()
                Database.add_product(product_name, price, quantity)
                self.display_menu()
                return self.main(self.get_menu_input())
            if user_input == 'b':
                Database.backup_database()
                self.display_menu()
                return self.main(self.get_menu_input())
            if user_input == 'q':
                self.clear_screen()
                Database.close_db_connection()
                sys.exit()
