#!/usr/bin/env python3

class Solution:
#    def longestCommonPrefix(self, strs: List[str]) -> str:
    def isCommonPrefix(self, strs,length):
        str0 = strs[0][:length]
        count = len(strs)
        for i in range( 1,count ):
            if str0 != strs[i][:length]:
                return False
        return True;

    def longestCommonPrefix(self, strs):
        minlen = min(len(s) for s in strs)
        left = 0
        right = minlen;

        while left < right:
            mid = (right - left + 1) //2 + left
            print(left,right,mid,strs[0][:mid]);
            if self.isCommonPrefix(strs,mid):
                left = mid
            else:
                right = mid - 1

        print(left)
        return strs[0][:left]

def main():
    s = Solution()
    strs = ["flower","flow","flight"]
    print(strs)
    print(s.longestCommonPrefix(strs))

if __name__ == '__main__':
    main()
