'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    print(n)
    #  n = integer used in __name__
    #  cache = integer (in this case, array) data stored in RAM

    # Your code here

    # if integer = 0, returns 1
    if n == 0:
        return 1
    # if integer is less than 0, returns 0
    elif n < 0:
        return 0

    # else if the cache and the chache array of n is greater
    # than 0, it stores the interger of n as the conctents of the cache.
    # Now, cache has a value
    elif cache and cache[n] > 0:
        return cache[n]
    # 
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    #  num_cookies takes the place of 'n' as shown in 'eating_cookies'
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
