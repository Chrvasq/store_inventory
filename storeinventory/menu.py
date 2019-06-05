from storeinventory.product import Product


class Menu:
    def __init__(self):
        self.menu_options = {'v': 'View product by product_id',
                             'a': 'Add a product to the inventory database',
                             'b': 'Backup database to a .CSV file'}
        self.product_name = None
        self.product_quantity = None
        self.product_price = None

    def view_product(self, product_id):
        product = Product.get_by_id(product_id)
        print(f'Product Name: {product.product_name}')
        print(f'Quantity: {product.product_quantity}')
        print(f'Price: ${product.product_price / 100:.2f}\n')
    
    def add_product(self):
        pass
    
    def backup_database(self):
        pass
    
    def display_menu(self):
        pass
    
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
                self.product_price = int(price.lstrip('$').replace('.', ''))
        except ValueError as error:
            print(error)
            self.get_product_price()


    def get_menu_input(self):
        pass

    def main(self):
        pass