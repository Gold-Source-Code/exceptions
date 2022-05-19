# /Values/
amount = 0
types = ["SmallPizza", "MediumPizza", "ItalianPizza", "FamilyPizza"]
order = {
    types[0] : 0,
    types[1] : 0,
    types[2] : 0,
    types[3] : 0
}

# /Prices/
Small = 3.99
Medium = 5.99
Italian = 8.49
Family = 11.99
# /Check/
def Limit(maxInt, Q):
    x = -1
    while x == -1:
        try:
            x = int(input(Q))
        except ValueError:
            print("Try again")
            x = -1
        if x <= maxInt and x > 0:
            break
        x = -1
        print("Try again")
    return x
# /Start/
def AskAmount():
    global amount
    amount = Limit(10, "How many pizza's do you want to order? ")
    SizeChecker()
# /Size/
def SizeChecker():
    global amount, order
    for x in range(0, amount):
        AddPizza = Limit(4, "Select Pizza: Small - 3.99 [1] | Medium - 5.99 [2] | Italian - 8.49 [3] | Family - 11.99 [4]")
        AddPizza = AddPizza - 1
        order.update({types[AddPizza]: order.get(types[AddPizza]) +1})
    print(order)
    Compile()
# /Price/
def Compile():
    TotalPrice = 0
    TotalPrice = TotalPrice + (3.99 * (order.get(types[0])))
    TotalPrice = TotalPrice + (5.99 * (order.get(types[1])))
    TotalPrice = TotalPrice + (8.49 * (order.get(types[2])))
    TotalPrice = TotalPrice + (11.99 * (order.get(types[3])))
    print("Your total is: " + str(TotalPrice))
# /Execute/
AskAmount()
