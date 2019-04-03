class Solution:
    def isStrobogrammatic(self, num:str) -> bool:
        start, end = 0, len(num) - 1
        while start <= end:
            if "".join(sorted(num[start]+num[end])) not in ["00","11","88","69"]:
                return False
            start += 1
            end -= 1
        return True

def main():
    print(Solution().isStrobogrammatic('69169'))
    #return True


if __name__ == '__main__':
    main()