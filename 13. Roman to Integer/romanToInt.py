class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(0, len(s)-1):
            cur = s[i]
            post = s[i+1]
            if d[cur]<d[post]:
                ans -= d[cur]
            else:
                ans += d[cur]
        ans += d[s[-1]]
        return ans
    
def main():
    print(Solution().romanToInt('MCMXCIV'))
    # return 1994

if __name__ == '__main__':
    main()