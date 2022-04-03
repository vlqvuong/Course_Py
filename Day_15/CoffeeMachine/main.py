MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def check_resource(order_ingredients):
    """Kiểm tra xem trong máy có đủ tài nguyên để làm loại cà phê đã chọn không"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
# Hàm này sẽ kiểm tra, nếu có 1 tài nguyên nào không đủ thì sẽ in ra có tài nguyên đó không đủ;


def cal_coins():
    """Tính toán giá trị các đồng xu đã nhập vào"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def compare_money(money_received, drink_cost):
    """Trả về True nếu tiền nhận lớn hơn giá cà phê chọn, ngược lại thì False"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
#         sử dụng biến global profit để tính số tiền có trong máy nếu bỏ tiền đủ giá cà phê.
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Giảm tài nguyên nếu làm loại cà phê đó cho user"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


continues = True
while continues:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        continues = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        # Ấn tổ hợp phím Alt + Shift và kéo chuột xuống các dòng giúp ta nhập dữ liệu giống nhau với nhiều dòng.
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = cal_coins()
            # Kiểm tra nếu đủ nguyên liệu thì tính số coin bỏ vào và tính tổng gán vào payment.
            if compare_money(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            # So sánh số tiền với giá cà phê. đủ thì làm cà phê.
