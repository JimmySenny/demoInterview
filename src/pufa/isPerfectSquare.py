#!/usr/bin/env python3

class Solution:
#    def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquare(self, num):
        if(num < 2):
            return True;
        i = 2
        while i<=num//2:
            if i*i == num:
                return True;
            i += 1;
        return False;

    def isPerfectSquare1(self, num):
        if(num < 2):
            return True;
        left = 2;
        right = num//2;
        while left <= right:
            x = left + (right-left+1)//2;
            guess = x * x;
            if guess == num:
                return True;
            if guess > num:
                right = x - 1;
            else:
                left = x + 1;
        return False;

def main():
    s = Solution();
    print(s.isPerfectSquare1(0));
    print(s.isPerfectSquare1(2));
    print(s.isPerfectSquare1(3));
    print(s.isPerfectSquare1(4));
    print(s.isPerfectSquare1(9));


if __name__ == '__main__':
    main();
