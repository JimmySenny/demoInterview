#!/usr/bin/env python3

class Solution:
    def reverse(self, x):
        if -10 < x < 10:
            return x
        strx = str(x)
        if strx[0] != "-":
            strx = strx[::-1]
            x = int(strx)
        else:
            strx = strx[:0:-1]
            x = int(strx)
            x = -x
        x = x if -2**31 < x < 2**31 -1 else 0
        return x

def main():
    s = Solution()
    num = "-12345"
    print(num[:0:-1])
    print(s.reverse(9111111111111111));

if __name__ == '__main__':
    main()

