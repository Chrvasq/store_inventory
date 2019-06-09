#!/usr/bin/env python3
from storeinventory.menu import Menu

if __name__ == "__main__":
    try:
        Menu().main()
    except KeyboardInterrupt:
        print('\nExiting application.\n')
