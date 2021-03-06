"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total, t = 1,1
    while t <= k:
        total = total* n
        n, t  = n - 1, t + 1
    return total
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    z, y = False, False
    while n > 0:
        k, n = n% 10, n//10
        if k == 8:
            z = True
            if n % 10 == 8:
                y = True
        if z and y:
            return True
    return False                 
                    

            
            
