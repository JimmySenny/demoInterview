#!/usr/bin/env python3

class Solution:
#    def moveZeroe(sself, nums: List[int]) -> None:
    def moveZeroe(sself, nums):
        len_nums = len(nums)
        left,right = 0,0
        while right < len_nums:
            print(left,right,nums)
            if nums[right] == 0:
                right += 1
            else:
                if left != right:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                left += 1
                right += 1
            
        return nums

def main():
    s = Solution()
    nums1 = [0,1,0,3,12]
    print(s.moveZeroe(nums1))

if __name__ == '__main__':
    main()


