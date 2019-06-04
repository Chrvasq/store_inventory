from storeinventory.product import Product


class Menu:
    def __init__(self):
        self.menu_options = {'v': 'View product by product_id',
                             'a': 'Add a product to the inventory database',
                             'b': 'Backup database to a .CSV file'}

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

    def get_user_input(self):
        pass

    def main(self):
        pass