#!/usr/bin/env python3

class Solution:
#    def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums):
        if len(nums) < 2:
            return nums[0]

        #1 排序
        nums = sorted(nums)

        #特例
        if( nums[0] != nums[1] ):
            return nums[0]

        if( nums[len(nums)-1] != nums[len(nums) -2] ):
            return nums[len(nums) - 1]

        #循环判断
        #for i in range( 1, len(nums)+1):
        #    if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
        #        return nums[i]
        for i in range( 0, len(nums),2):
            if nums[i] != nums[i+1]:
                return nums[i+1]

    def singleNumber1(self, nums):
        while True:
            num = nums[0]
            nums.remove(num)
            try:
                nums.remove(num)
            except:
                return num



def main():
    s = Solution();
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))

    print(s.singleNumber1([2,2,1]))
    print(s.singleNumber1([4,1,2,1,2]))
if __name__ == '__main__':
    main()
