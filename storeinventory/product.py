from peewee import *

db = SqliteDatabase('inventory.db')


class Product(Model):
    product_id = AutoField()
    product_name = TextField(unique=True)
    product_price = IntegerField()
    product_quantity = IntegerField()
    date_updated = DateField()

    class Meta:
        database = db
