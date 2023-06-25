def binPowRec(a,b):

    if b == 0:
        return 1
    
    res = binPowRec(a, b//2)
    # If b is odd
    # If b % 2 == 1
    if b % 2:
        return res * res * a
    else:
        return res * res


# pow(a,b) in O(log n)
def binPow(a, b):

    res = 1

    while b > 0:
        # b << 1 = b * 2
        # b >> 1 = b/2
        # If b & 1 = b % 2 
        # If b % 2 == 1
        if b & 1:
            res = res * a

        a = a * a

        # b >> 1  = b//2
        # b >> 2  = b//4
        # b >> 3  = b//8
        # b >> 4  = b//16
        b >>= 1

    return res
