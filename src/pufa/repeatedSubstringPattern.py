#!/usr/bin/env python3

class Solution:
#    def repeatedSubstringPattern(self, s: str) -> bool:
    def repeatedSubstringPattern(self, s):
        ss = s + s;
        if s in ss[1:-1]:
            return True;
        return False;

def main():
    s = Solution();
    print(s.repeatedSubstringPattern("abab"));
    print(s.repeatedSubstringPattern("aba"));
    print(s.repeatedSubstringPattern("abcabcabcabc"));
    print(s.repeatedSubstringPattern("abba"));

if __name__ =='__main__':
    main();
