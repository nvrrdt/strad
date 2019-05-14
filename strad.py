def calc(x):
    factors = []
    i = 2
    while i < x:
        while x % i == 0:
            x /= i
            factors += [i]
        i += 1
    return factors

def get_large(x):
    return calc(x)[-1] #return the last factor in the list


print ("The largest factor is: " +str(get_large(600851475143)))