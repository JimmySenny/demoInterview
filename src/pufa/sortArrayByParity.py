#!/usr/bin/env python3

class Solution:
#    def sortArrayByParity(self, A: List[int]) -> List[int]:
    def sortArrayByParity(self, A):
        i = 0
        j = len(A) - 1
        while i < j:
#4 种情况针对 (A[i] % 2, A[j] % 2)：
#如果是 (0, 1)，那么万事大吉 i++ 并且 j--。
#如果是 (1, 0)，那么交换两个元素，然后继续。
#如果是 (0, 0)，那么说明 i 位置是正确的，只能 i++。
#如果是 (1, 1)，那么说明 j 位置是正确的，只能 j--。
            if( A[i]%2 > A[j]%2):
                A[i],A[j] = A[j],A[i]
            if A[i]%2 == 0:
                i += 1;
            if A[j]%2 == 1:
                j -= 1;
        return A
    #按照2的模排序 冒泡
    def sortArrayByParity1(self, A):
        i, j = 0, 0;
        while i < len(A) - 1:
            flag = False
            j = 0
            while j < len(A) - 1 - i:
                if(A[j]%2 > A[j+1]%2):
                    A[j],A[j+1] = A[j+1],A[j]
                    flag = True;
                j += 1
            if not flag:
                break
            i += 1
        return A;            
    def sortArrayByParity2(self, A):
        #按照2的模排序 选择
        i,j,index = 0,0,0
        while i < len(A) - 1:
            index = i
            j = i + 1
            while j < len(A):
                if(A[j]%2 > A[index]%2):
                    index = j
                j += 1
            if index != j:
                tmp = A[i]
                A[i] = A[index]
                A[index] = tmp

            i += 1
        return A

def main():
    s = Solution();
    a = [3,1,2,4];
    print(s.sortArrayByParity2(a))
    print(s.sortArrayByParity2([2,6,3,5]))
    print(s.sortArrayByParity2([2,6,3,5,6]))

if __name__ == '__main__':
    main();
