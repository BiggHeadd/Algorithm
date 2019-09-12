# coding:utf-8

class Solution(object):
    # s 源字符串
    def replaceSpace(self, s):
        if not s:
            return ""

        result = []
        for word in s:
            if word == " ":
                result.append("%20")
            else:
                result.append(word)
        return "".join(result)

if __name__ == "__main__":
    solution = Solution()
    s = "We Are Happy."
    answer = solution.replaceSpace(s)
    print(answer)