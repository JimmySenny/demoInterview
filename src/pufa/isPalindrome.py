#!/usr/bin/env python3

class Solution:
#    def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        nl,nr = [],[];
        nl = str(x)
        nr = str(x)[::-1]
        if( nl == nr ):
            return True;
        return False;
    def isPalindrome1(self, x):
        if( x < 0 ):
            return False;
        
        while( x >=10):
            div = 1;
            while(x // div >= 10 ):
                div *= 10;
            left = x//div
            right = x % 10;
            print(left,right,x,div)
            #left = 1, right = 1 left != right  判断是False
            if not (left == right):
                return False;
            x = (x%div)//10;
            print(x)
        return True;


def main():
    s = Solution();
    print(s.isPalindrome(121));
    print(s.isPalindrome(-121));
    print(s.isPalindrome(10));
    print(s.isPalindrome(1000021));

    print(s.isPalindrome1(1221));
    print(s.isPalindrome1(12321));
    print(s.isPalindrome1(123421));
    print(s.isPalindrome1(1000021));

if __name__ == '__main__':
    main();
