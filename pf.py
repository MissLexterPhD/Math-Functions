import math_methods

def run(a):
    a, b = math_methods.prime_factorize(a)
    print("Prime Factors, Power: ", end="")
    for i in range(len(a)):
        if i != len(a)-1:
            print("(" + str(a[i]) + ", " + str(b[i]), end="); ")
        else:
            print("(" + str(a[i]) + ", " + str(b[i]) + ")")
