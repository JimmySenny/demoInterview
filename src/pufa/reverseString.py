#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 切片
class Solution:
#    def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s):
        #s = s[::-1];
        s[0::] = s[::-1];
    def reverseString1(self,s):
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

def main():
    l = [ "h","e","l","l","o" ];
    s = Solution();
    print( s.reverseString(l) );
    print( l );

    print( s.reverseString1(l) );
    print( l );
if __name__ == '__main__':
    main();
