# First, what is the smallest in lexicographical order?
# Just like dictionary, a < aa < ab < bd < bef.
# 
# This idea is made by StefanPochmann.
# 

class Solution:
    def removeDuplicateLetters(self, s:str) -> str:
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

def main():
    #print(Solution().removeDuplicateLetters('bcabc'))
    # return abc
    print(Solution().removeDuplicateLetters('cbacdcbc'))
    # 'abcd', but it should return 'acdb'

if __name__ == '__main__':
    main()
