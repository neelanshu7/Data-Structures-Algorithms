// https://leetcode.com/problems/power-of-two/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        for (int i=0;i<31;i++){
            // int ans=pow(2,i);
            if(n==pow(2,i)){
                return true;
            }
        }
        return false;
    }
};
