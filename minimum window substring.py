class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a = {}
        for i in t:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        b = {}
        c = 0
        d = len(a)
        l = 0
        x = 1000000
        y = ""
        for r in range(len(s)):
            if s[r] in b:
                b[s[r]] += 1
            else:
                b[s[r]] = 1

            if s[r] in a and b[s[r]] == a[s[r]]:
                c += 1

            while c == d:
                if r - l + 1 < x:
                    x = r - l + 1
                    y = s[l:r + 1]

                b[s[l]] -= 1

                if s[l] in a and b[s[l]] < a[s[l]]:
                    c -= 1

                l += 1

        return y