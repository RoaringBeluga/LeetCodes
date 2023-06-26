"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""
from copy import deepcopy

test_1 = (
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
)

test_2 = (
    [""],
    [[""]]
)

test_3 = (
    ["a"],
    [["a"]]
)

tests = [
    test_1,
    test_2,
    test_3
]


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    a_list = deepcopy(strs)

    while len(a_list):
        item = a_list.pop()
        key = tuple(sorted(item))
        if key in anagrams.keys():
            anagrams[key].append(item)
        else:
            anagrams[key] = [item]

    return sorted([sorted(item) for item in anagrams.values()], key=len)  # sorted(anagrams.values(), key=len)


if __name__ == '__main__':
    for test, expected in tests:
        result = group_anagrams(test)
        print(f"Test data: {test}")
        print(f"Test result: {result}")
        print(f"Expected result: {expected}")
        print(f"Verdict: {'PASSED' if result == expected else 'FAILED'}")
