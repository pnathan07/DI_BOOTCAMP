#challenge 1
# Ask the user for a word
word = input("Enter a word: ")

# Create a dictionary to store the indexes of each letter
indexes_dict = {}

# Iterate over each letter in the word
for index, letter in enumerate(word):
    # Convert the index to a string
    index_str = str(index)
    
    # Check if the letter is already a key in the dictionary
    if letter in indexes_dict:
        # Append the index to the list of indexes
        indexes_dict[letter].append(index_str)
    else:
        # Create a new list with the index and assign it to the letter key
        indexes_dict[letter] = [index_str]

# Print the dictionary
print(indexes_dict)

#challenge 2 
def clean_price(price):
    return int(price.replace("$", "").replace(",", ""))

def affordable_items(items_purchase, wallet):
    wallet_amount = int(wallet.replace("$", ""))
    affordable_items = [item for item, price in items_purchase.items() if clean_price(price) <= wallet_amount]
    affordable_items.sort()
    return affordable_items if affordable_items else "Nothing"

# Test cases
items_purchase_1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet_1 = "$300"
print(affordable_items(items_purchase_1, wallet_1))  # ➞ ["Bread", "Fertilizer", "Water"]

items_purchase_2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet_2 = "$100"
print(affordable_items(items_purchase_2, wallet_2))  # ➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

items_purchase_3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet_3 = "$1"
print(affordable_items(items_purchase_3, wallet_3))  # ➞ "Nothing"
