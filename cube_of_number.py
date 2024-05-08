#cube of a number
# 2*2*2 = 8

num = int(input("Enter valur for num :"))

i = 1
result = 1
while i<= 3:
    result *= num
    print(result, "when i is", i)
    i = i + 1

    print("Result of a cube :",result)

# cube of first-10 numbers
    cube = 1
    for i in range(1, 11, 1):
        cube = i*i*i
        print(i, "*", i, "*", i, "=", cube)