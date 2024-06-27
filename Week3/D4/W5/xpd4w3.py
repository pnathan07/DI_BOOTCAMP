#-- Part 1 
#create table menu_items (
#	item_id serial primary key 
#	item_name varchar(30) not null,
#	item_price smallint default 0
#);
import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def save(self):
        conn = psycopg2.connect(dbname="restaurant", user="your_username", password="your_password")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))
        conn.commit()
        cursor.close()
        conn.close()
    
    def delete(self):
        conn = psycopg2.connect(dbname="restaurant", user="your_username", password="your_password")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cursor.close()
        conn.close()
    
    def update(self, new_name, new_price):
        conn = psycopg2.connect(dbname="restaurant", user="your_username", password="your_password")
        cursor = conn.cursor()
        cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s", (new_name, new_price, self.name))
        conn.commit()
        cursor.close()
        conn.close()
        self.name = new_name
        self.price = new_price

import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(dbname="restaurant", user="your_username", password="your_password")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        item = cursor.fetchone()
        cursor.close()
        conn.close()
        if item:
            return MenuItem(item[1], item[2])
        return None
    
    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(dbname="restaurant", user="your_username", password="your_password")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Menu_Items")
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return [MenuItem(item[1], item[2]) for item in items]

#Part 2
# menu_editor.py

from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMenu:")
        print("V: View an Item")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("S: Show the Menu")
        print("E: Exit")
        choice = input("Please choose an option: ").upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            show_restaurant_menu()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    try:
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)
    try:
        item.delete()
        print("Item was deleted successfully.")
    except Exception as e:
        print(f"Error deleting item: {e}")

def update_item_from_menu():
    current_name = input("Enter the current name of the item: ")
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = MenuItem(current_name, 0)
    try:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    except Exception as e:
        print(f"Error updating item: {e}")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nRestaurant Menu:")
    for item in items:
        print(f'Item: {item.name}, Price: {item.price}')

def view_item():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f'Item: {item.name}, Price: {item.price}')
    else:
        print("Item not found.")

if __name__ == "__main__":
    show_user_menu()
