# arbitrary arguments functions
def total(* args):
    sum = 0
    for i in args:
        sum = sum + i

    print("Summation : ", sum)


total(1,2,3,4,5,6,7,8,9,10)


 
    