class Solution:
    def read(self, buf: List[str], n: int) -> int:
        cnt = 0
        tmp = [""]*4
        while cnt < n:
            r = read4(tmp)
            if r == 0:
                break
            for i in range(min(r, n - cnt)):
                buf[cnt] = tmp[i]
                cnt += 1
        return cnt