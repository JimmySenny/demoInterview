#!/usr/bin/env python3

class Solution:
#    def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
    #暴力匹配
        lens = len(s)
        if lens <= 1:
            return s
        len_max = 1;
        ans = s[0]
        i = 0
        while i < lens:
            j = i + 1
            while j < lens+1:
                print(i,j,s[i:j],s[i:j][::-1])
                if j - i > len_max and s[i:j] == s[i:j][::-1]:
                    len_max = j - i
                    ans = s[i:j]
                j += 1
            i += 1;
        return ans
    def longestPalindromeDP(self, s):
        #动态规划
        lens = len(s)
        if lens < 2:
            return s
#        dp = [ [F] * lens ] * lens;
        #使用列表创建一个二维数组，可以使用生成器来辅助实现。
        #list_three = [[0 for i in range(3)] for j in range(3)]
        dp = [["F" for i in range(0,lens)] for j in range(0,lens) ]


        len_max = 1;
        left = 0;
        j = 0
        while j < lens:
            i = 0
            while  i <= j:
                if i == j:
                    dp[i][j] = "T";
                elif s[i] == s[j]:
                    #没有子串
                    if j - i < 3: 
                        dp[i][j] = "T" 
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = "F";

                print( i,j,dp[i][j], j-i+1, len_max );
                if dp[i][j] == "T":
                    len_curr = j - i + 1; # len = right - left + 1
                    if len_curr > len_max:
                        len_max = len_curr;
                        left = i
                i += 1;
            j += 1;

        for i in range (0,lens):
                print(dp[i]);

        return s[left:left+len_max]


def main():
    s = Solution();
#    print(s.longestPalindrome("babad"))
    print(s.longestPalindromeDP("babad"))
    print(s.longestPalindromeDP("cbbd"))
    print(s.longestPalindromeDP("aaaa"))
    print(s.longestPalindromeDP("bbbbb"))

if __name__ == '__main__':
    main();
