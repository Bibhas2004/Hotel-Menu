menu={
    'Chicken Pizza':50,
    'Fish Pizza':60,
    'Panner Pizza':40,
    'Chicken Burger':70,
    'Panner Burger':55,
    'Salad':20,
    'Coffee':30,
    'Moktail':35,
}
print("Welcome to Das Restaurant")
print("Chicken Pizza: 50/-\nFish Pizza: 60/-\nPanner Pizza: 40/-\nChicken Burger: 70/-\nPanner Burger: 55/-\nSalad: 20/-\nCoffee: 30/-\nMoktail: 35/-")

order_total=0

item_1=input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

anoter_item=input("Do you add another item?(Yes/No) ")
if anoter_item=="Yes": 
    item_2=input("Enter the name of the next item you want to order: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")
print(f"The total amount of item to pay is {order_total}")
print(f"Thank you!")