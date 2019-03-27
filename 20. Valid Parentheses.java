/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        top = -1
        stack = []
        brackets = {'{':'}', '(':')', '[':']'}
        
        for c in s:
            if brackets.get(c) is not None:
                stack.append(c)
                top+=1
            else:
                if top<0:
                    return False
                top_c = stack.pop(top)
                top-=1
                if brackets.get(top_c)!=c:
                    return False
        if top >= 0:
            return False
        else:
            return True
