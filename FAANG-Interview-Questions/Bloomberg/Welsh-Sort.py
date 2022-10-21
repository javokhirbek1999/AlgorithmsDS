"""
Time: O(n)
Space: O(n)
"""
def solve(string):
    alphabet = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
    alpha_index = {ch:index for index, ch in enumerate(alphabet)}

    i = 0

    res = []

    while i < len(string)-1:

        if string[i]+string[i+1] in alpha_index:
            res.append(alpha_index[string[i] + string[i+1]])
            i += 2
        else:
            res.append(alpha_index[string[i]])
            i += 1
        
    if i < len(string):
        res.append(alpha_index[string[-1]])
    
    
    return tuple(res)
