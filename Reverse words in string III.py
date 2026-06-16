class Solution(object):
    def reverseWords(self, s):
        r = ""
        slow = 0
        for fast in range(len(s) + 1):
            if fast == len(s) or s[fast] == " ":
                string = s[slow:fast]
                r += string[::-1]
                if fast != len(s):
                    r += " "
                slow = fast + 1
        return r
