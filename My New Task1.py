#add 2 data parameter
#sub 2 data parameter
#mul 2 data parameter
#div 2 data parameter


def add(num1, num2):
    total = number1 + number2
    return total

def sub(num1, num2):
    total = number1 - number2
    return total

def mul(num1, num2):
    total = number1 * number2
    return total

def div(num1, num2):
     total = number1 / number2
     return total

number1 = int(input("Enter Number: "))
number2 = int(input("Enter Number: "))
operator = input("Enter Operation: ")


match operator:
    case"+":
        print(add(number1, number2))

    case"-":
        print(sub(number1, number2))
        
    case"*":
        print(mul(number1, number2))
        
    case"/":
        print(div(number1, number2))
