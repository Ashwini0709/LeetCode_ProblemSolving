class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int={"I" :1, "V" :5, "X" :10, "L" :50, "C" :100, "D" :500, "M" :1000}
        result = 0
    
        for i, roman in enumerate(s):
            j = len(s) - 1
            if i == j:
                result = result + roman_int[roman]
            elif roman_int[roman] >= roman_int[s[i+1]]:
                result = result + roman_int[roman]
            else:
                result = result - roman_int[roman]
                
        return result
