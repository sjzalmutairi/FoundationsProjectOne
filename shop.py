####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Wake and Bake" #complete me!""
signature_flavors = ["espresso", "biscuit", "maple"] #complete me!
order_list = []


def print_menu():
    print("Our menu:")
    for item in menu:
        print("- \"%s\" (KD %s)" % (item, menu[item]))

def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print("- \"%s\"" % item)

def print_signatures():
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print("- \"%s\"" % item)





def is_valid_order(order):
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return False

def get_order():
    
    order_list = []

    order = input("What is your order? (Enter the exact spelling of the item you would like. Type 'Exit' to end your order.)\n")

    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()

    return order_list


def accept_credit_card(total):
   
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    
    total = 0

    for order in order_list:
        order = order.lower()
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price
    

    return total


def print_order(order_list):
    
    print()

    print("Your order is: ")

    for order in order_list:
        print("- %s " % order)
        
    print()
       
    price = get_total_price(order_list)

    print("That will be KD %s" % price)

    if accept_credit_card(price):
        print("This order is eligible for credit card payment.")


    print("Thank you for shopping at %s" % cupcake_shop_name)
