"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

{i: x for x, i in enumerate(list1)}

"""
import collections


def firstUniqChar(s):
    unique_str_map = {}
    prev_chars = {}


    for i, char in enumerate(s):

        if prev_chars.__contains__(char) and unique_str_map.__contains__(char):
            unique_str_map.pop(char)

        elif not prev_chars.__contains__(char):
            unique_str_map[char] = i
            prev_chars[char] = i

    if unique_str_map == {}:
        return -1
    return list(unique_str_map.values())[0]


a = firstUniqChar("opopl")
print(a)
