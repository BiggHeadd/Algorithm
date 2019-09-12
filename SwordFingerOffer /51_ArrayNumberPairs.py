# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        count = self.InversePairsCore(data[:], 0, len(data) - 1, data[:])
        return count % 1000000007

    def InversePairsCore(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        elif end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        middle = (start + end) // 2
        cnt = self.InversePairsCore(data, start, middle, tmp) + self.InversePairsCore(data, middle + 1, end, tmp)

        i = start
        j = middle + 1
        index = start

        while i <= middle and j <= end:
            if data[i] <= data[j]:
                tmp[index] = data[i]
                i += 1
            else:
                tmp[index] = data[j]
                j += 1
                cnt += middle - i + 1
            index += 1

        while i <= middle:
            tmp[index] = data[i]
            index += 1
            i += 1
        while j <= end:
            tmp[index] = data[j]
            index += 1
            j += 1
        return cnt


if __name__ == "__main__":
    data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    solution = Solution()
    result = solution.InversePairs(data)
    print(result)
    print(data)
    print(data[:])