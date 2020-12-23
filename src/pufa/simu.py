#!/usr/bin/env python3

import sys
class Solution:
    def simu(self, nums,nums_in):
        print(nums,nums_in)
        for i in range( len(nums_in) ):
            try:
                nums.remove(nums_in[i])
            except:
                print(nums_in[i])
        return nums    

def main():
    nums = [1,2,3]

    #一行输入一行数据，然后没有规定我要输入多少行，你要自行判断文件结束EOF
#    while True:
#        line = sys.stdin.readline()
#        if not line or line = '\n':
#            break

    #一行输入多个数字，并以空格隔开
    nums_in = [] 
    ss = input("请输入数值，用空格隔开:")
    data = ss.split(" ")
    i = 0
    while i < len(data):
        if data[i].isdigit():
            #print(data[i])
            nums_in.append(int(data[i]))
        i += 1

    s = Solution();
    print(s.simu(nums,nums_in))

if __name__ == '__main__':
    main()
