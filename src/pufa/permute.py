#!/usr/bin/env python3

class Solution:
#    def permute(self, nums: List[int]) -> List[List[int]]:
    def backtrack( self, nums, path, check, res ):
        print("path", path, check)
        if len(nums) == len(path):
            res.append(path.copy())
            print("res", res)
            path = []
            return

        i = 0
        while i < len(nums):
            if check[i]:
                i += 1
                continue;
            check[i] = True
            path.append(nums[i])
            print("i", i, "path", path, check)
            self.backtrack(nums, path, check,res)
            check[i] = False;
            path.pop()
            i += 1;

    def permute(self, nums):
        if len(nums) == 0:
            return [];

        check = [False for _ in range(len(nums))]
        print(check)
        res = []

        self.backtrack(nums, [], check, res )

        return res;
        

def main():
    nums = [1,2,3]
    s = Solution();
    print(s.permute(nums))

if __name__ == '__main__':
    main()
