import math_methods

def run(a, b, c):
    x = math_methods.roots(a, b, c)
    if x == "DNE":
        print("No real solutions")
    else:
        print("Roots: " + str(x[0]) + ", " + str(x[1]))
    
