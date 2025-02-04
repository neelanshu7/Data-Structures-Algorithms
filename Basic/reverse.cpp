// https://leetcode.com/problems/reverse-integer/
class Solution {
public:
    int reverse(int x) {
        long rev=0;
        if(x==0 || x/10==0){
            return x;
        }else{
            while(x!=0){
                rev=(rev*10)+x%10;
                x=x/10;
                if (rev > INT_MAX || rev < INT_MIN) return 0;
            }
            return rev;
        }
    }
};
