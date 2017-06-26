import csv

# Displays the inventory in the simplest way


def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print (value, key)
    print("Total number of items: ", sum(inventory.values()))

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order):
    longest = len(max(inventory, key=len))
    align_right = "{:>%d}    {:>%d}" % (longest, longest)
    print("Inventory:")
    print(align_right.format("count", "item name"))
    print("-" * longest * 3)
    if order == "count,asc":
        sorted_list = sorted(list(set(inventory.values())))
    elif order == "count,desc":
        sorted_list = sorted(list(set(inventory.values())), reverse=True)
    elif order is None:
        sorted_list = list(set(inventory.values()))
    else:
        print ("Invalid ordering method")
        exit()
    for number in (sorted_list):
        for key, value in inventory.items():
            if number == value:
                print (align_right.format(value, key))
    print("-" * longest * 3)
    print("Total number of items: ", sum(inventory.values()))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, filename):
    if filename is None:
        filename = "import_inventory.csv"
    with open(filename, "r") as csvfile:
        for row in csv.reader(csvfile):
            add_to_inventory(inventory, row)
    return inventory

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename):
    list_to_export = []
    if filename is None:
        filename = "export_inventory.csv"
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in inventory.items():
            for howmanyitem in range(value):
                list_to_export.append(key)
        writer.writerow(list_to_export)


"""
def display_inventory(inventory):
    print("Inventory:")
    for i in inventory:
        print (i,end=" ")
        print (inventory.get(i))
    print("Total number of items: ", sum(inventory.values()))

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv,dragon_loot)
print_table(inv,"count,desc")
export_inventory(inv, None)
import_inventory(inv,"export_inventory.csv")
print_table(inv,"count,desc")"""
