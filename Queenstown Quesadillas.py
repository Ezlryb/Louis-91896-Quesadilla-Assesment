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



def print_menu():
    """Returns the menu as a string"""
    os.system('clear')
    message = ""
    for i, thing in enumerate(quesadilla_menu):
        if i == 0:
            message += ("\n     **** Queenstown Quesadillas ****\n\n")
        elif i == 8:
            message += ("\n\n    **** Extas menu ****\n\n")
        message += (f"({i+1}) {thing[0]}  ${thing[1]}\n {thing[2]}\n")

    return message

        


def main():
    """While loop with all the user's options"""
    while True:
        choice = get_int(print_menu() + "\nWhat would you like to order?", 1, 8) - 1 # choice equals the users chosen item's index in the quesadilla_menu list
        

main()
