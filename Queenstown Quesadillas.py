"""Queenstown Quesadillas is a program to automate the odering prcess for a quasadillas resturaunt in queenstown"""
import os, math

yes_inputs = ["yes", "y"]
no_inputs = ["no", "n"]
date = [8, 4, 2025] #day, month, year
months_2d = [
    ["1", "01", "jan", "january"],
    ["2", "02", "feb", "february"],
    ["3", "03", "mar", "march"],
    ["4", "04", "apr", "april"],
    ["5", "05", "may"],
    ["6", "06", "jun", "june"],
    ["7", "07", "jul", "july"],
    ["8", "08", "aug", "august"],
    ["9", "09", "sep", "sept", "september"],
    ["10", "oct", "october"],
    ["11", "nov", "november"],
    ["12", "dec", "december"]
]
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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
    """inputs question that will be repeated in between clears (clears all other text.)Returns the users input if it is an integer between upper and lower"""
    os.system('clear')
    while True:
        num = input(question + "\n> ")
        os.system('clear')
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



def get_expected_input(question, possible_inputs):
    """inputs question and a lsit of valid inputs and loops until the users answer is one of the possible inputs then returns that as a string"""
    while True:
        answer = input(question)
        if answer in possible_inputs:
            return answer
        else:
            input("Invalid input, press enter to continue\n\n> ")


def card_num():
    """Returns card number as int"""
    while True:
        number = get_int("Please enter your card number", 0, 999999999999999)
        if str(number).len() <= 9:
            print("Please enter a valid card number of at least nine digits.")
        else:
            return number


def year():
    """Returns card's expiration year as int"""
    return get_int("What year does your card expire?", 1950, 2050)


def month():
    """Returns card's expiration month in 1, 2 ect. format as int"""
    while True:
        month = input("What mouth does it expire in?")
        for i in range(12):
            if month in months_2d[i]:
                print(i)
                return i
        os.system('clear')
        print("Please enter a valid month!\n\n")


def day():

    get_int("What day of the mouth is it in") 


def checkout():
    card_num()
    temp_month = month()
    if date[0] >= temp_month():
        print()
    



    
    






def menu():
    """Returns the menu as a string"""
    os.system('clear')
    message = "\n     **** Queenstown Quesadillas ****\n\n"
    for i, thing in enumerate(quesadilla_menu):
        if i == 8:
            message += ("\n\n    **** Extas Menu ****\n\n")
        message += (f"\n({i+1}) {thing[0]}  ${thing[1]}\n {thing[2]}\n") # eg (1) Classic Quesadilla

    return message



def cart():
    """Return's ui for cart as well as all your items"""
    message = "\n\n    **** Cart ****\n\n"
    total = 0
    for i, item in enumerate(order):
        message += f"Item {i+1}: {item[0]} ${item[1]}\n"
        total += item[1]
    message += f"\nTotal: ${round(total, 2)}"
    return message
    


def main():
    """While loop with all the user's options"""
    while True:
        choice = get_int(menu() + "\nWhat would you like to add to your order? (Enter 0 to go to cart!)", 0, 11) - 1 # choice equals the users chosen item's index in the quesadilla_menu list
        os.system('clear')
        if choice == -1:
            if len(order) != 0:
                print(cart())
                choice = get_int("Press (1) to check out\nPress (2) to remove items/extras from your order\nPress (3) to return to menu.", 1, 3)
                if choice == 1:
                    checkout()
                elif choice == 2:
                    pass
                elif choice == 3:
                    continue

            else:
                input("You have no items in your cart!\nPress Enter to Continue\n\n> ")
                continue

        elif choice <= 7:
            num_of_quesadillas = get_int(f"How many {quesadilla_menu[choice][0]}s would you like?", 0, 10)
            if input(f"Add {num_of_quesadillas} {quesadilla_menu[choice][0]}(s) ${quesadilla_menu[choice][1]*num_of_quesadillas} to cart? (y/n)").lower().strip() in yes_inputs:
                for i in range(num_of_quesadillas):
                    order.append(quesadilla_menu[choice].copy())
                order.sort()
        elif choice >= 8:
            if len(order) != 0:
                item_index = get_int(f"\nWhich item would you like to add {quesadilla_menu[choice][0]} to?\n\n{cart()} ", 1, len(order))-1
            else:
                input(f"You have no items to add {quesadilla_menu[choice][0].lower()} to in your cart!\n\nPress Enter to Continue\n\n> ")
                continue

            if quesadilla_menu[choice][0] in order[item_index][0]:
                input(f"You have already added {quesadilla_menu[choice][0]} to this item\n\nPress Enter to continue\n\n> ")
            else:
                order[item_index][0] += " + " + quesadilla_menu[choice][0]
                order[item_index][1] += quesadilla_menu[choice][1]
                order.sort()
            input(f"{cart()}\n\n Press enter to return to menu\n\n> ")


main()
