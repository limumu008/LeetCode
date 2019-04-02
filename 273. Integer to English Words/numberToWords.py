class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n: int) -> str:
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]]+['Hundred']+words(n%100)
            for p,w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

def main():
    print(Solution().numberToWords(1234567))
    #return "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

if __name__ == '__main__':
    main()