# items available in the vending machine
items=[
    {"item number":1,"item": "Water Bottle", "Price":2},
    {"item number":2, "item": "Coffee", "Price": 2},
    {"item number":3, "item": "Apple Juice","Price": 4},
    {"item number":4, "item":"Cola","Price": 2},
    {"item number":5, "item": "Mango Juice","Price": 5},
    {"item number":6, "item":"Chips", "Price": 2.50},
    {"item number":7, "item":"Corroisant", "Price": 3},
    {"item number":8, "item":"Chocolate", "Price": 2.50},
    {"item number":9, "item":"Gummy", "Price": 5},
    {"item number":10, "item":"PopCorn", "Price": 3.50}
]
#display items
print("Items Available:")
for item in items:
    print(f"{item['item number']}. {item['item']} - AED {item['Price']}")

#asking users choice of items
user_input=int(input("enter item number:"))

#check if the items exist
for item in items:
    if item["item number"] == input:
        print("item is being dispensed ")

#find the price of that item
for item in items:
    if item["item number"] == user_input:
        price = item["Price"]
print("Item is being prepared")

#asking user for money
amount = int(input("insert item amount(AED):"))

#analyze the amount given by the user
if amount >= price:
    print("Payment successful")
    change = amount - price  # returning change to the user
    print("Change returned:",change)
    print("The item has been dispensed")
else:
    print("amount denied!")