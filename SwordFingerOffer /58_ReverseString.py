# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""

        s = list(s)
        start = 0
        end = len(s) - 1
        s = self.Reverse(s, start, end)

        start = end = 0
        while start < len(s):
            print(start, end, len(s))
            if s[start] == " ":
                start += 1
                end += 1
            elif end == len(s) or s[end] == " ":
                print(s)
                s = self.Reverse(s, start, end - 1)
                start = end + 1
                end += 1
            else:
                end += 1
        return "".join(s)

    def Reverse(self, s, start, end):
        while end > start:
            s[end], s[start] = s[start], s[end]
            start += 1
            end -= 1
        return s


if __name__ == "__main__":
    solution = Solution()
    string = "I am a student."
    result = solution.ReverseSentence(string)
    print(result)