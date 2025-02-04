// https://leetcode.com/problems/palindrome-number/
class Solution {
public:
    bool isPalindrome(int x) {
        long num,rev=0;
        num=x;
        while(num!=0){
            rev=(rev*10)+num%10;
            num=num/10;
        }
        if(x==rev and x>=0){return true;}
        else{return false;}
    }
    
};
