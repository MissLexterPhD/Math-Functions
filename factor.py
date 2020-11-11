import math_methods

def run(a):
    a = math_methods.factors(a)
    print("Factors: ", end="")
    for i in range(len(a)):
        if i != len(a)-1:
            print(a[i], end=", ")
        else:
            print(a[i])
