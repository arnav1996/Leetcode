#Given a string, find the length of the longest substring without repeating characters.

/*Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/     
             
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s==null) return 0;
        if(s.length()==1) return 1;
        int length=0;
        int currentLength=0;
        boolean[] array=new boolean[256];
        for(int j=0; j<s.length()-1;j++ ){
            array=new boolean[256];
            currentLength=0;
            for(int i=j;i<s.length();i++){
                if(!array[s.charAt(i)]){
                    array[s.charAt(i)]=true;
                    currentLength++;
                    if(currentLength>length){
                        length=currentLength;
                    }
                }
                     else{
                         break;
                     }
                    
                    
                }
            }
        
    
   return length; 
    }
    
}
