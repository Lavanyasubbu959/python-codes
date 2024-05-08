# list and maths operations

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
result = 0
avg = 1
for i in list[:10]:
    result += i
    avg = (result/10)

print("sum : ",result)
print("Average : ", avg)

# in and not in are membership operators
print(numbers)
print(30 in numbers)
print(60 in numbers)
print(40 not in numbers)