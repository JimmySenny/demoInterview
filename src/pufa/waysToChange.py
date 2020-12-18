#!/usr/bin/env python3

class Solution:
#    def waysToChange(self, n: int) -> int:
    def waysToChange(self, n):
        print("n:",n)
        dp = [0] * (n+1);
        coins = [1,5,10,25]
        dp[0] = 1

        for coin in coins:
            print("coin:",coin)
            for i in range(coin,n+1):
                dp[i] = dp[i] + dp[i-coin]
                print("i:",i,dp)

        print(dp[n], dp[n]%1000000007);
        return dp[n]%1000000007

def main():
    s = Solution();
    print(s.waysToChange(5))
    print(s.waysToChange(10))

if __name__ == '__main__':
    main()
