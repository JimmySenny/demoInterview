#!/usr/bin/env python3

class Solution:
#    def addBinary(self, a: str, b: str) -> str:
    def addBinary(self,a,b):
        if not a or not b:
            return '';
        a = a[::-1];
        b = b[::-1]
        ans = [];

        carry = 0;
        i = 0;
        j = 0;
        mlen = len(a) if len(a) > len(b) else len(b);

        while i < mlen or carry:
            n1 = int(a[i]) if i < len(a) else 0;
            n2 = int(b[i]) if i < len(b) else 0;
            n = n1 + n2 + carry;
            carry = 1 if n > 1 else 0;
            ans.append(str(n%2));
            i += 1;
        return ''.join(ans[::-1]);

def main():
    s = Solution();
    s1 = "1111"
    s2 = "1111"
    print(s.addBinary(s1,s2));

if __name__ == '__main__':
    main()
