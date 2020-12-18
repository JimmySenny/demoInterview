#!/usr/bin/env python3
'''

罗马数字    阿拉伯数字
M   1000
CM  900
D   500
CD  400
C   100
XC  90
L   50
XL  40
X   10
IX  9
V   5
IV  4
I   1
'''

class Solution:
#    def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        value = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < 13:
            print("index,num:", index,num)
            while num >= key[index]:
                res += value[index]
                num -= key[index]
                print("num,key,value:", num,key[index],value[index])
            index += 1                    
        return res

def main():
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(5))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))

if __name__ == '__main__':
    main()
