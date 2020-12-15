#!/usr/bin/env python3

#两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离
class Solution:
#    def hammingDistance(self, x: int, y: int) -> int:
    def hammingDistance(self, x, y):
        sum = 0;
        while(x != 0 or y != 0):
            if( (x & 1) != (y & 1)):
                sum += 1;
            x = x >> 1;
            y = y >> 1;
        return sum

def main():
    s = Solution();
    print(s.hammingDistance( 9, 11));
    print(s.hammingDistance( 1, 4));


if __name__ == '__main__':
    main()
