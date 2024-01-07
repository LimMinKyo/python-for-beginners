def tax_calculator(money):
    return money * 0.35


def pay_tax(tax):
    print("Thank you for paying", tax)


to_pay = tax_calculator(150)
pay_tax(to_pay)
