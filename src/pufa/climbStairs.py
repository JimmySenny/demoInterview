#!/usr/bin/env python3

class Solution:
#    def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        #递归
        if n == 1 or n == 2:
            return n;
        a,b,tmp = 1,2,0;
        for i in range(3,n+1):
            temp = a + b;
            a = b;
            b = temp;
        return temp;
    def climbStairsDP(self, n):
        #动态规划
        dp = [0] * (n+1);
        dp[0] = 1
        dp[1] = 1
        i = 2
        while i < n + 1:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1

        return dp[n]

def main():
    s = Solution();
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(5))
    print(s.climbStairs(9))
    print(s.climbStairs(11))
    print(s.climbStairs(15))

    print(s.climbStairsDP(1))
    print(s.climbStairsDP(2))
    print(s.climbStairsDP(3))
    print(s.climbStairsDP(5))
    print(s.climbStairsDP(9))
    print(s.climbStairsDP(11))
    print(s.climbStairsDP(15))

if __name__ == '__main__':
   main()
