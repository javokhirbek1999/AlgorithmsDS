"""
Time: O(n)
Space: O(n)
"""
def solve(s: str) -> str:

    s = list(s)

    hour1 = s[0]
    hour2 = s[1]

    minute1 = s[3]
    minute2 = s[4]

    if hour1 == '?':
        if hour2 <= '3' or hour2 == '?':
            s[0] = '2'
        else:
            s[0] = '1'
    
    if hour2 == '?':
        s[1] = '9' if hour1 < '2' else '3'
    
    if minute1 == '?':
        s[3] = '5'
    
    if minute2 == '?':
        s[4] = '9'
    

    return "".join(s)
