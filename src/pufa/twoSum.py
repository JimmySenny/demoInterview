#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #正常解法
    def twoSum(self, nums, target):
        i = 0;
        j = 0;
        result = []
        while (i < len(nums) -1 ):
            j = i+1;
            while( j < len(nums) and j <= nums[j] ):
                if (nums[i] + nums[j]) == target:
                    result.append(nums[i]);
                    result.append(nums[j]);
                j += 1;
            i += 1;
        return result;
    def twoSum_ptr(self, nums, target):
        i = 0;
        j = len(nums) -1;
        while i < j:
            if( nums[j]>= target or nums[i] + nums[j] > target ):
                j -= 1;
            elif( nums[i] + nums[j] < target ):
                i += 1;
            else:
                return nums[i], nums[j]
        return [];


def main():
    s = Solution();
    print( s.twoSum([2,7,11,15], 9));
    print( s.twoSum([10,26,30,31,47,60], 43));
    print( s.twoSum_ptr([2,7,11,15], 9));
    print( s.twoSum_ptr([10,26,30,31,47,60], 43));

if __name__ == '__main__':
    main();
