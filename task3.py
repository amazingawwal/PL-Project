#1. Calculate Discount Function
def calculate_discount1(price, discount_percent):
    if discount_percent >= 0.2:
        return price * discount_percent
    return price

final_price = calculate_discount1(50, 0.3)
print(f"Final Price: {final_price}")


# 2. Calculate Discount Function with user prompt
def calculate_discount(price, discount_percent):

    if discount_percent >= 0.2:
        return price * discount_percent
    return price

price = input('Enter the price: ')
price = int(price)
discount = input("Enter the discount percentage from '0.1 - 1': ")
discount = float(discount)
final_price = calculate_discount(price, discount)
print(f"Final Price: {final_price}")