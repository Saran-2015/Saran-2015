

https://github.com/user-attachments/assets/cb2c4d6e-0d5d-4c4d-b9d6-2ff7ea0ab47f

# Inventory-Manager
An inventory management system using Flask

## Getting Started

- Features
  1. [Adding Products and Locations](#adding-products-and-locations)
  2. [Deleting Products and Locations](#deleting-products-and-locations)
  3. [Moving Products](#moving-products)
  4. [Editing Products and Locations](#editing-products-and-locations)

### Prerequisites

To run this system you will need :

- Python 3
- Flask
- sqlite3

## System Summary

This system is built to simulate a warehouse environment and handles balancing quantities over warehouses. It has 4 main views including *Overview*,*Products*,*Locations* and *Transfers*. **Products** and **Locations** let you add,edit and delete entries from the system. **Transfers** lets you move items into the central warehouse, out of the central warehouse; also to and from various locations.It also displays transfer history. **Overview** will display products,warehouses and their respective balanced quantities.

## Features

### Adding Products and Locations
Products require product name and quantity to be filled. Location only requires location name



### Moving products
Here products can be moved to a location, from a location as well as to and from a location. Products need to initially be added to various locations from the central warehouse.


### Editing Products and Locations
Change in product or loaction name creates changes in their names in the history and system overview.So, you can rectify a spelling error and still not loose any data.


# Built using
- Flask
- Python
-sqlite3

