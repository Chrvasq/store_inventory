#!/usr/bin/env python3
from storeinventory.etl import (Product, db, extract_and_clean_data,
                                transform_data, add_data_from_csv)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    add_data_from_csv(transform_data('inventory.csv'))
