"""
Time: O(n * log x)
Space: O(1)
"""
def feas(a, m, diff):
    l = a[0]
    i = 0
    for _ in range(m - 1):
        while i < len(a) and a[i] < l + diff:
            i += 1
        if i == len(a):
            return False
        l = a[i]
    
    return True

def globalMaximum(a, m):
    i, j = 0, a[-1] - a[0]
    while i < j - 1:
        mid = (i + j) // 2
        
        if feas(a, m, mid):
            i = mid
        else:
            j = mid - 1
            
    return j if feas(a, m, j) else i
