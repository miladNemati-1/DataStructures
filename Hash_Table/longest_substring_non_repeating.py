
""""
Longest Substring Without Repeating Characters

Solution
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

# #my solution


# def lengthOfLongestSubstring(s: str) -> int:
#     loop = len(s)
#     counter = 0

#     letter_hash_map = set()
#     largest_set = set()
#     while counter < loop:
#         if s[counter] not in letter_hash_map:
#             letter_hash_map.add(s[counter])
#         else:
#             s = s[1:]
#             loop = len(s)
#             counter = -1
#             letter_hash_map = set()
#         if len(largest_set) < len(letter_hash_map):
#             largest_set = letter_hash_map
#         counter += 1

#     return len(largest_set)


"""
better solution
"""




import collections
def lengthOfLongestSubstring(s: str) -> int:
    chars = collections.Counter()

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res


print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("dvdf"))
# print(lengthOfLongestSubstring("jbpnbwwd"))
# print(lengthOfLongestSubstring("aab"))
