/*
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
*/

class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) <= (len(A) - 1) #if A and B are same, check if string contains dup characters
        else:
            temp = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    temp.append(i)
                if len(temp) > 2:
                    return False
            return len(temp) == 2 and A[temp[0]] == B[temp[1]] and A[temp[1]] == B[temp[0]]
