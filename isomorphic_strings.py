"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

"aaeaa"
"uuxyy"
"""


class Solution:
    def keys_map_the_same(self, s, t):
        string_dict = {}
        for i in range(len(s)):
            if string_dict.__contains__(s[i]):
                if string_dict[s[i]] != t[i]:
                    return False
            else:
                string_dict[s[i]] = t[i]
        return True

    def isIsomorphic(self, s, t):
        return self.keys_map_the_same(s, t) and self.keys_map_the_same(t, s)


a = Solution()
answer = a.isIsomorphic(s="aaeaa", t="uuxyy")
print(answer)
