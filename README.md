# Store Inventory

This Store Inventory console application provides a user with a menu
including options to view products, add products and backup the Sqlite3 database to
a .csv file.

# Requirements
- Python 3.7
- Peewee 3.9.4

# Installation
You will need to install pipenv if you don't already have it installed.

You can find more information on how to install pipenv
[here](https://pypi.org/project/pipenv/)

Install dependencies and run the app.

```sh
$ cd store_inventory
$ pipenv install --ignore-pipfile
$ pipenv run python app.py
```

# Future Features
- Ability to add multiple products from .csv file
- Delete products
- View all products in a paginated list
