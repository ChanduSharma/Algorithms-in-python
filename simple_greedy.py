'''Given an infinite number of quarters  (25cents) , 
   dimes(10cents) , nickels (5cents) , and pennies (1cent) , 
   implement a function to calculate 
   the minimum number of coins to represent v cents.
'''

def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    res = []
    for i in reversed(coins_available):
        if i > v:
            continue

        res.extend([i]*(v//i))
        v = v % i

    return res


result = find_min_coins(19, [1, 5, 10, 25])

assert result == [10, 5, 1, 1, 1, 1]
print(result)
