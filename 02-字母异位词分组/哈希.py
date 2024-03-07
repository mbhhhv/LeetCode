class Solution:
    def groupAnagrams(self, strs:list[str])->list[str]:
        dic = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
            'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
            'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
            'y': 97, 'z': 101
        }
        dic_map = {}
        result = []
        for str in strs:
            res = 1
            for i in range(0, len(str)):
                res = res * dic[str[i]]
            if res not in dic_map:
                dic_map[res] = []
            dic_map[res].append(str)
        for value in dic_map.values():
            result.append(value)
        return result

s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

'''
给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。字母异位词是由重新排列源单词的所有字母得到的一个新单词。

示例1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]

示例2:
输入: strs = [""]
输出: [[""]]

示例3:
输入: strs = ["a"]
输出: [["a"]]
'''