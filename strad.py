import secrets, binascii

basket = [] # a basket of hashes from transactions

for i in range(10):
    basket.append(secrets.token_hex(15)) # mockup of those hashes

sum_basket = 0

for i in basket:
    sum_basket = sum_basket + int(i, 16) # sum of all the hex hashes in the basket

def calc(x): # framework for finding the factors of a number
    factors = []
    i = 2
    while i <= x/2:
        if (x % i == 0):
            factors.append(i)
            print(factors)
        i = i + 1
        if (i == 10000000): # break after these cycles to move on faster
            break
    return factors

def get_large(x): # idem framework, find largest factor
    return calc(x)[-1] #return the last factor in the list

largest_factor = get_large(sum_basket)

for i in basket:
    if (int(i, 16) % largest_factor == 0):
        print("ok")
    else:
        print("nok")

# print(get_large(sum_basket))