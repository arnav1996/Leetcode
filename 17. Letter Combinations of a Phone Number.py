/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

*/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
         if digits == None or digits == "":
            return []

         num_to_letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
         try :
            possible_letters = [num_to_letter[digit] for digit in digits]
         except KeyError: 
            return []

         ans = []
         for comb in itertools.product(*possible_letters, repeat = 1):
            # print(itertools.product(possible_letters))
            ans.append(''.join(comb))
         return ans

