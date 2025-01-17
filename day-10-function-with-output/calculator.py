def add(n1, n2) :
    return n1 + n2

def substract(n1, n2) :
    return n1 - n2

def multiply(n1, n2) :
    return n1 * n2

def divide(n1, n2) :
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
def calculator() :
    num1 = float(input("What's the first number : "))

    for symbol in operations :
        print(symbol)

    end= False

    while not end :
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")

        if should_continue == 'y' :
            num1 = answer
        else :
            end = True
            calculator()

calculator()