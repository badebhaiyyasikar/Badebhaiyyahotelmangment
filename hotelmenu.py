#define the menu of bade bhaiyya hotel
menu={
    'pizza':99,
    'burger':89,
    'noodles':79,
    'pasta':89,
    'frenchfries':89,
    'coffee':40,
    }

#greet
print("welcome to bade bhaiyya hotel")
print("pizza : Rs99\nburger : Rs89\nnoodles : Rs79\npasta : Rs89\nfrenchfries : Rs89\ncoffee : Rs40")

oder_total=0


item_1=input("enter the name of item of you want to order =")
if item_1 in menu:
    oder_total+=menu[item_1]
    print(f"your item {item_1} has been added to your oder")

else:
    print("orderd item {item_1} is not available yet")

another_order=input("do you want to order another item? (yes/no) ")
if another_order=='yes':
    item_2=input("enter the name of item of you want to order =")
    if item_2 in menu:
        oder_total+=menu[item_2]
        print(f"your item {item_2} has been added to your oder")

    else:
        print("orderd item {item_2} is not available yet")

    another_order=input("do you want to order another item? (yes/no) ")
    if another_order=='yes':
        item_3=input("enter the name of item of you want to order =")
        if item_3 in menu:
            oder_total+=menu[item_3]
            print(f"your item {item_3} has been added to your oder")

        else:
            print("orderd item {item_3} is not available yet")

    else:
        print("orderd item {item_2} is not available yet")
print(f"your total amount of items to pay is {oder_total}")