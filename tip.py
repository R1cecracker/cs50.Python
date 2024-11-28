# defines main function
def main():
    # asks user for the price of the meal
    dollars = dollars_to_float(input("How much was the meal? "))
    # asks user how much they would like to tip in a percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # calculates how much to tip
    tip = dollars * percent
    # prints the amount to tip
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # removes "$" from value
    d = d.replace("$", "")
    # returns new value
    return float(d)


def percent_to_float(p):
    # removes "%" from value
    p = p.replace("%", "")
    # returns new value and divides by 100 for percentage
    return float(p)/100


main()