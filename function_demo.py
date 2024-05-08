# function demo

# function with no parameters and no return value
def addition():
    num1 = int(input("Enter value for num1 : "))
    num2 = int(input("Enter value for num2 : "))
    result  = num1 + num2
    print("Result of Addition : ",result)

# function with parameter but no return value
def subtraction(x, y):
    result = x - y
    print("Result of Subtraction : ",result)

# function with no parameter but return value
def division():
    n1 = int(input("Enter valur for n1 : "))
    n2 = int(input("Enter valur for n2 : "))
    result = n1 // n2
    return result

# function with parameter and return value
def multiplication(a, b):
    return a * b

addition()
x = int(input("Enter value for x : "))
y = int(input("Enter valur for y : "))
subtraction(x, y)

tempResult = division()
print("Result of division : ", tempResult)

a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))
tempResult = multiplication(a, b)
print("Result of multiplication : ", tempResult)