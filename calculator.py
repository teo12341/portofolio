def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("Type the first number:"))
    accumulate = True

    while accumulate:
        for symbols in operations:
            print(symbols)
        symbol = input("Type a mathematical operation:")
        num2 = float(input("Type the second number:"))
        answer = operations[symbol](num1, num2)
        print(f"The answer is: {num1} {symbol} {num2} = {answer}")
        choice = input(f"Type 'yes' to calculate with {answer} or 'no' to start a new calculation:")

        if choice == "yes":
            num1 = answer
        else:
            accumulate = False
            calculator()

calculator()


