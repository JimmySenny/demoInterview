#!/usr/bin/env python3
class Solution:
#    def generate(self, numRows: int) -> List[List[int]]:
    def generate(self, numRows):
        ret = list();
        i = 0
        while i < numRows:
            row = list();
            j = 0
            while j < i+1:
                if j == 0 or j == i:
                    row.append(1);
                else:
                    row.append(ret[i-1][j] + ret[i-1][j-1]);
                j += 1
            i += 1
            ret.append(row);
        return ret;

def main():
    s = Solution()
    print(s.generate(5));
    print(s.generate(10));

if __name__ == '__main__':
    main()
