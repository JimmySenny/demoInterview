#!/usr/bin/env python3

class Solution:
#    def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs(self,nums,lens,depth,path,used,res):
        if depth == lens:
            res.append(path[:])
            return
        i = 0
        while i < lens:
            if not used[i]:
                used[i] = True
                path.append(nums[i])

                self.dfs(nums,lens,depth+1,path,used,res)

                used[i] = False;
                path.pop()

    def permute(self, nums):
        lens = len(nums)
        if lens == 0:
            return [];

        used = [False for _ in range(lens)]
        res = []
        self.dfs(nums,lens,0,[],used,res)
        return res;
        


def main():
    s = Solution();
    print(s.permute([1,2,3,4]))

if __name__ == '__main__':
    main()
