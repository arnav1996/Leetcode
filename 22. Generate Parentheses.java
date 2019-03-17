/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/


class Solution {
    
    List <String> combinations= new ArrayList<>();
    
    public List<String> generateParenthesis(int n) {
        
        generateParenthesis(n,n, "");
        return combinations;
        
    }
    
    private void generateParenthesis(int open, int closed, String s){
        if(open==0 && closed==0){
            combinations.add(s);
        }
        
        else{
            if(open>0){
                generateParenthesis(open-1,closed,s+"(");
                
            }
            if(closed>0 && closed>open){
                generateParenthesis(open,closed-1,s+")");
            }
        }
    }
}
