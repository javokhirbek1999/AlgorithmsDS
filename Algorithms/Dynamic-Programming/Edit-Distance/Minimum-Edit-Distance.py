"""
Time: O(n^2)
Space: O(n^2)
"""

def minEditDistance(str1: str, str2: str, m: int, n: int):
    
    dp = []

    for _ in range(m+1):
        row = []
        for _ in range(n+1):
            row.append(0)
        dp.append(row)

    
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, 
            # only option is to copy all letters of second string
            if i == 0:
                dp[i][j] = j
            
            # If second string is empty,
            # only option is to copy all letters of first string
            elif j == 0:
                dp[i][j] = i
            
            # If characters of both strings match,
            # just skip it
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take the minimum number of distance 
                # of all operations
                dp[i][j] = 1 + min(
                    dp[i][j-1], # inserted
                    dp[i-1][j], # removed
                    dp[i-1][j-1] # replaced
                )
    
    return dp[m][n]


def main():
    
    str1 = "abc"
    str2 = "bcc"

    res = minEditDistance(str1, str2, len(str1), len(str2))

    print(res)


if __name__ == "__main__":
    main()
