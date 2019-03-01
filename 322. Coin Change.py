/*You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
*/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dic = {}
        for c in coins:
            dic[c] = 1
        for v in range(1,amount+1):
            for s in coins:
                diff = v - s
                if v - s in dic:
                    if v not in dic:
                        dic[v] = dic[v-s] +1
                    else:
                        dic[v] = min(dic[v],dic[v-s]+1)
        if amount not in dic:
            return -1
        else:
            return dic[amount]
