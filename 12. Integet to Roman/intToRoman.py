class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        for val, roman in [(1000, 'M'), (900, 'CM'), (500, 'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'LX'),(5,'V'),(4,'IV'),(1,'I')]:
            count = num//val
            if count: 
                ans += count*roman
                num -= count*val
            if not num:
                return ans

def main():
    print(Solution().intToRoman(1994))
    # return "MCMXCIV"

if __name__ == '__main__':
    main()