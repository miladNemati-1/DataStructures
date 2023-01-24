"""
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".


"""


class Solution:
    def findRestaurant(self, list1, list2):
        larger_list = list2
        if len(list1) >= len(list2):
            larger_list = list1
        answer = []
        hash_map1 = {i: x for x, i in enumerate(list1)}
        hash_map2 = {i: x for x, i in enumerate(list2)}
        min = [len(larger_list), len(larger_list)]
        for item in larger_list:
            if hash_map1.__contains__(item) and hash_map2.__contains__(item):
                if hash_map1[item] + hash_map2[item] < sum(min):
                    min = [hash_map1[item], hash_map2[item]]
                    if list1[hash_map1[item] == list2[hash_map2[item]]]:
                        answer = [list1[hash_map1[item]]]
                    else:
                        answer = [list1[hash_map1[item]],
                                  list2[hash_map2[item]]]
                elif hash_map1[item] + hash_map2[item] == sum(min):
                    answer.append(list1[hash_map1[item]])

        return answer


sol = Solution()
answer = sol.findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"])
print(answer)
