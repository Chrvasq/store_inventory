#!/usr/bin/env python3
from storeinventory.etl import (Product, db, extract_data,
                                transform_data, load_data)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    load_data(transform_data('inventory.csv'))
