"""Queenstown Quesadillas is a program to automate the odering prcess for a quasadillas resturaunt in queenstown"""
import os, random, math

quesadilla_menu = [
    ["Classic Quesadilla", 7.99, "A crispy, golden tortilla stuffed with a blend of melted cheddar and Monterey Jack cheese. Served with sour cream and salsa."],
    ["Chicken Quesadilla", 9.99, "Grilled chicken, melted cheese, and sautéed peppers, folded into a warm tortilla. Served with sour cream and salsa."],
    ["Steak Quesadilla", 11.99, "Tender grilled steak, gooey cheese, and caramelized onions, all toasted to perfection. Served with sour cream and guacamole."],
    ["BBQ Pulled Pork Quesadilla", 10.99, "Slow-cooked pulled pork smothered in tangy BBQ sauce, paired with melted cheese and crispy tortilla. Served with ranch dressing."],
    ["Buffalo Chicken Quesadilla", 10.99, "Spicy buffalo chicken and creamy cheese blend, grilled inside a crispy tortilla. Served with ranch or blue cheese."],
    ["Veggie Quesadilla", 8.99, "A fresh mix of sautéed mushrooms, bell peppers, onions, and zucchini with melted cheese. Served with guacamole and salsa."],
    ["Breakfast Quesadilla", 9.99, "Scrambled eggs, crispy bacon, and cheddar cheese, grilled to perfection. Served with salsa and sour cream."],
    ["Supreme Quesadilla", 12.99, "A loaded combination of grilled chicken, steak, sautéed veggies, and cheese, all wrapped in a golden tortilla. Served with sour cream, salsa, and guacamole."],
    ["Extra Cheese", 1.00, "Add an extra layer of gooey, melted cheese to any quesadilla."],
    ["Guacamole", 1.50, "A side of fresh, creamy guacamole for dipping or topping."],
    ["Jalapeños", 0.75, "Spice things up with sliced jalapeños, perfect for an extra kick."]
]
order = []


def get_int(question, lower, upper):
    """Returns the users input if it is an integer between upper and lower"""
    while True:
        num = input(question + "\n> ")
        try:
            if int(num) >= lower and int(num) <= upper and str(int(num)) == num:
                return int(num)
            else:
                int("")

        except ValueError:
            if upper == math.inf:
                if lower == -math.inf:
                    print(f"Enter a whole number!!!")
                else:
                    print(f"Enter a whole number above {lower}!!!")

            elif lower == -math.inf:
                print(f"Enter a whole number between {lower} and {upper}!!!")
            else:
                print(f"Enter a whole number between {lower} and {upper}!!!")



def menu():
    """Returns the menu as a string"""
    os.system('clear')
    message = "\n     **** Queenstown Quesadillas ****\n\n"
    for i, thing in enumerate(quesadilla_menu):
        if i == 8:
            message += ("\n\n    **** Extas Menu ****\n\n")
        message += (f"({i+1}) {thing[0]}  ${thing[1]}\n {thing[2]}\n") # eg (1) Classic Quesadilla

    return message


def cart():
    """Return's ui for cart as well as all your items"""
    message = "\n\n    **** Cart ****\n\n"
    for i, item in enumerate(order):
        message += f"Item {i}: {item[0]} (${item[1]})"
    return message

        


def main():
    """While loop with all the user's options"""
    while True:
        choice = get_int(menu() + "\nWhat would you like to add to your order? (Enter 0 to go to cart!)", 0, 11) - 1 # choice equals the users chosen item's index in the quesadilla_menu list
        os.system('clear')
        if choice == -1:
            if len(order) >= 0:
                print(cart())
            else:
                print("You have no items in your cart!")
            input("\nPress Enter to Continue\n\n> ")    
        elif choice <= 7:
            temp_order = []
            num = get_int(f"How many {quesadilla_menu[choice][0].lower()}s would you like?", 0, 10)
            if input(f"Add {num} {quesadilla_menu[choice][0].lower()}(s) ${quesadilla_menu[choice][1]*num} to cart? (y/n)").lower().strip() in ["y", "yes", "yeah", "yup"]:
                for i in range(num):
                    temp_order.append(quesadilla_menu[choice][0])
                    order.append(temp_order)
                    order.sort()
        if choice >= 9:
            get_int(f"{cart()} Which item would you like to add {quesadilla_menu[choice][0]} to?", 1, len(order))

        checkout = get_int(f"{cart} \n\nPress 0 to checkout press 1 to return to menu", 0, 1)

main()
