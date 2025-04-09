"""Queenstown Quesadillas is a program to automate the ordering prcess for a quasadillas resturaunt in queenstown"""
import os, math

yes_inputs = ["yes", "y"]
no_inputs = ["no", "n"]
date = [4, 2025] #day, month, year
months_2d = [
    ["1", "01", "jan", "january"],
    ["2", "02", "feb", "february"],
    ["3", "03", "mar", "march"],
    ["4", "04", "apr", "april"],
    ["5", "05", "may", "may"],
    ["6", "06", "jun", "june"],
    ["7", "07", "jul", "july"],
    ["8", "08", "aug", "august"],
    ["9", "09", "sept", "september"],
    ["10", "10", "oct", "october"],
    ["11", "11", "nov", "november"],
    ["12", "12", "dec", "december"]
]
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
menu_length = 8 # increase by one for every quesadilla added or decrease if one is removed (this variable indicates where the extras menu has started)
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
] # name, price, discriptioin
order = []




def name_case(message):
    """Asks for name with message and returns the name with capitals and spaces if its has no symbols or numbers"""
    os.system('clear')
    while True:
        error = False
        name = input(message)
        new_name = []
        cap = True
        if name == "":
            input("Please enter a valid name!\n\nPress enter to continue\n\n> ")
            continue
        for letter in name:
            if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
                if cap:
                    new_name.append(letter.upper())
                    cap = False
                else:
                    new_name.append(letter.lower())            
            else:
                if letter == " ":
                    new_name.append(letter)
                    cap = True
                else:
                    os.system('clear')
                    print("Please do not enter any symbols or numbers!")
                    error = True
                    break
        if not error:
            name = ""
            for letter in new_name:
                name += letter
            return name



def get_int(question, lower, upper):
    """inputs question that will be repeated in between clears (clears all other text.)Returns the users input if it is an integer between upper and lower"""
    os.system('clear')
    while True:
        num = input(question + "\n> ")
        os.system('clear')
        try:
            if int(num) >= lower and int(num) <= upper and num.find(".") == -1:
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
        answer = input(question).lower()
        if answer in possible_inputs:
            return answer
        else:
            input("Invalid input, press enter to continue\n\n> ")



def card_num():
    """Returns card number as int"""
    os.system('clear')
    while True:
        number = input("Please enter your card number\n> ")
        try:
            int(number)
        except ValueError:
            os.system('clear')
            print("Please enter a number!")
            continue
        if len(str(number)) <= 8:
            os.system('clear')
            print("Please enter a valid card number of at least nine digits!")
        else:
            return number



def year():
    """Returns card's expiration year as int"""
    return get_int("What year does your card expire?", 1950, 2050)



def month():
    """Returns card's expiration month in 1, 2 ect. format as int"""
    while True:
        message = "Eg. ("
        for month_name in months_2d:
            message += month_name[2] + ", "
        message = message[:-2] + ")"


        month = input(f"What month does it expire in?\n{message}\n\n> ").lower()
        for i in range(12):
            if month in months_2d[i]:
                return i
        os.system('clear')
        print("Please enter a valid month!\n\n")



def security_code():
    os.system('clear')
    while True:
        security_code = input("Please enter your security code\n> ")
        try:
            int(security_code)
            if len(str(security_code)) == 3:
                return security_code
        except ValueError:
            pass
        os.system('clear')
        print("Please enter a valid three-digit code!")



def checkout():
    """Prints checkout menu and gets the users information"""
    boolean = True
    while boolean:
        card_name = name_case("Please enter the card holders name\n> ").strip()
        num = card_num().strip()
        code = security_code().strip()
        expiry_year = year()
        expiry_month = month()
        os.system('clear')
        if date[1] == expiry_year:
            if date[0] <= expiry_month:
                input("This card has expired!\n\nPress enter to continue\n\n> ")
                continue
        elif date[1] > expiry_year:
            input("This card has expired!\n\nPress enter to continue\n\n> ")
            continue
        while True:
            answer = input(f"Is this information correct? (y/n)\n\n{card_name}\n{num}  {code}\n{months_2d[expiry_month][1]}/{expiry_year}\n\n> ").lower()
            if answer in yes_inputs:
                boolean = False
                break
            if answer in no_inputs:
                boolean = True
                break
            else:
                os.system('clear')
                print("Please enter a valid input!")
            
    total = 0
    for item in order:
        total += item[1]
    answer = get_int(f"Please choose one:\n\n(1) Pickup ${total} \n(2) Delivered ${total + 10}\n(3) Cancel order", 1, 3)
    if answer == 1:
        print(f"Your order will be ready in roughly {len(order)} minutes!")
    elif answer == 2:
        adress = input("Please enter your full adress (please note if you live outside Queenstown Basin we will not be able to deliver your order)\n\n> ")
        os.system('clear')
        answer = input(f"Is this adress correct? (y/n) \n\n{adress}\n\n> ")
        os.system('clear')
        if answer in no_inputs:
            print("Thats a shame :(")
        print("Your order is on its way!\n")
    else:
        return



def menu():
    """Returns the menu as a string"""
    os.system('clear')
    message = "\n     **** Queenstown Quesadillas ****\nCall us at 027-000-000-0000\n\n"

    for i, thing in enumerate(quesadilla_menu):
        if i == menu_length:
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
    global order 
    while True:
        menu_choice = get_int(menu() + "\n\nWhat would you like to add to your order? (Enter 0 to go to cart!)", 0, len(quesadilla_menu)) - 1 # choice equals the users chosen item's index in the quesadilla_menu list
        os.system('clear')
        if menu_choice == -1:
            if len(order) != 0:
                while True:
                    print(cart())
                    cart_choice = get_int(f"{cart()}\n\nCheck out (1)\nRemove items (2)\nReturn to menu (3)", 1, 3)
                    if cart_choice == 1:
                        checkout()
                        input("Press enter to place anouther order!")
                        order = []
                    elif cart_choice == 2:
                        remove_choice = get_int(f"{cart()}\n\nWhich item would you like to remove?", 1, len(order))
                        del order[remove_choice-1]                        
                    elif cart_choice == 3:
                        break

            else:
                input("You have no items in your cart!\nPress Enter to Continue\n\n> ")
                continue

        elif menu_choice <= menu_length-1:
            num_of_quesadillas = get_int(f"How many {quesadilla_menu[menu_choice][0]}s would you like?", 0, math.inf)
            os.system('clear')
            while True:
                answer = input(f"Add {num_of_quesadillas} {quesadilla_menu[menu_choice][0]}(s) ${quesadilla_menu[menu_choice][1]*num_of_quesadillas} to cart? (y/n)\n\n> ").lower().strip()
                if answer in yes_inputs:
                    for i in range(num_of_quesadillas):
                        order.append(quesadilla_menu[menu_choice].copy())
                    order.sort()
                    break
                elif answer in no_inputs:
                    break
                else:
                    os.system('clear')
                    print("Please enter a valid input!")

        elif menu_choice >= menu_length:
            if len(order) != 0:
                item_index = get_int(f"\nWhich item would you like to add {quesadilla_menu[menu_choice][0]} to?\n\n{cart()} ", 1, len(order))-1
            else:
                input(f"You have no items to add {quesadilla_menu[menu_choice][0].lower()} to in your cart!\n\nPress Enter to Continue\n\n> ")
                continue

            if quesadilla_menu[menu_choice][0] in order[item_index][0]:
                input(f"You have already added {quesadilla_menu[menu_choice][0]} to this item\n\nPress Enter to continue\n\n> ")
            else:
                order[item_index][0] += " + " + quesadilla_menu[menu_choice][0]
                order[item_index][1] += quesadilla_menu[menu_choice][1]
                order.sort()
            input(f"{cart()}\n\n Press enter to return to menu\n\n> ")


main()
