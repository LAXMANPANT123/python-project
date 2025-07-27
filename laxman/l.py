menu = {
    'pizza' : 50,
    'pasta' : 50,
    'burger' : 60,
    'salad' : 70,
    'coffee' : 80,
}

print("welcome to the restaurant")
print("pizza: 50\n pasta: 50\n burger: 60\n salad: 70\n coffee: 80\n")

order_total = 0

item_1 = input("enter the name of the item you wnat to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order = input("do you wnat to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")

    else:
        print(f"ordered item {item_2} is not available yet!")

print(f"your total amount to pay is {order_total}")

    
