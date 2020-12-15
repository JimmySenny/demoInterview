#!/usr/bin/env python3

class Solution:
#    def mySqrt(self, x: int) -> int:
    def mySqrt(self, x):
        if( x < 1 ):
            return 0;
        i = 1
        ans = 1
        while(i <= (x+1)//2):
            if( i * i > x ):
                ans = i - 1;
                break;
            if( i * i == x ):
                ans = i
                break;
            i += 1;
        return ans;

    def mySqrt1(self, x):
        if( x < 1 ):
            return 0;
        left = 1
        right = (x + 1)//2
        while left < right:
            midright = (left + right + 1)//2
            print( "[",x, left, right, midright, "]" );
            guess = midright * midright;
            if( guess > x ):
                right = midright - 1;
            else:
                left = midright
        return left;


def main():
    s = Solution();
    print(s.mySqrt1(1));
    print(s.mySqrt1(2));
    print(s.mySqrt1(3));
    print(s.mySqrt1(4));
    print(s.mySqrt1(8));
    print(s.mySqrt1(9));
    print(s.mySqrt1(11));
    print(s.mySqrt1(36));


if __name__ == '__main__':
    main();
