class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =='':
            return 0 
        maxn = 0
        s = s.replace(' ','')
        if s == '':
            return 1

        def search(remain, now):
            if remain == "":
                return now

            i = remain[0]

            if judge(now, i):
                remain_n = remain[1:]
                now_n = now + i
                return search(remain_n, now_n)

            else:
                return now

        def judge(s, one):
            if s == '':
                return True
            for i in s:
                if not i != one:
                    return False
            return True

        for i in range(len(s)):
            st = s[i:]
            n = search(st, "")
            if (n != None) and maxn < len(n):
                maxn = len(n)

        return maxn