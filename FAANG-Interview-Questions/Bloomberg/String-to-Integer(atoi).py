class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        
        """
        1. ^ matches beginging of string 
        2. \s* any nunber of whitspaces (zero or more)
        3. [+-] either a + or -
        4. [+-]? zero or one of either +/-
        5. \d a digit 
        6. \d + one or more digit
        7. the the pattern inside () is a group where you can access 
        """
        
        
        REGEX = r'^\s*([-+]?\d+)'
        
        MAX = 2147483647
        MIN = -2147483648
        
        if not re.search(REGEX, string):
            return 0
        
        num = int(re.findall(REGEX, string)[0])
        
        return min(MAX, max(num, MIN))
