from peewee import *

db = SqliteDatabase('inventory.db')


class Product(Model):
    product_id = AutoField(primary_key=True)
    product_name = TextField()
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateField()

    class Meta:
        database = db
