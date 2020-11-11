import math

def factors(x):
    ret = [1]
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            ret.append(i)
    rev = ret.copy()
    rev.reverse()
    if not x == 1:
        for i in rev:
            if int(x/i) not in ret or i == 1:
                ret.append(int(x/i))
    return ret



def is_prime(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True


def prime_factorize(x):
    all_factors = factors(x)
    pruned_factors = all_factors[1:len(all_factors)]
    prime_factors = []

    powers = []
    for factor in pruned_factors:
        if not is_prime(factor):
            continue
        prime_factors.append(factor)
        powers.append(1)
        for power in range(2, int(math.log(x,factor))+1):
            if x % (factor**power) == 0:
                powers[-1] = power

    return prime_factors, powers
                

def lcm(a, b):
    a_fact, a_powers = prime_factorize(a)
    b_fact, b_powers = prime_factorize(b)
    big_factors = []
    big_powers = []
    for i in range(len(a_fact)):
        if a_fact[i] in b_fact:
            big_factors.append(a_fact[i])
            big_powers.append(max(a_powers[i], b_powers[i]))
        else:
            big_factors.append(a_factor)
            big_powers.append(a_powers[i])
    for i in range(len(b_fact)):
        if b_fact[i] not in big_factors:
            big_factors.append(b_fact[i])
            big_powers.append(b_powers[i])

    ret = 1
    for i in range(len(big_factors)):
        ret *= big_factors[i]**big_powers[i]
    return ret
    


def gcf(a, b):
    b_fact = factors(b)
    a_fact_rev = factors(a)
    a_fact_rev.reverse()
    for i in a_fact_rev:
        if i in b_fact:
            return i
    # just in case
    return 1
    

def roots(a, b, c):
    if b**2-4*a*c < 0:
        return "DNE"
    small = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    big = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    return small, big
