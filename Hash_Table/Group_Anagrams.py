

import collections


def groupAnagrams(strs):

    string_group_dict = {}
    for string in strs:
        ordered_string = ''.join(sorted(string))
        if string_group_dict.__contains__(ordered_string):
            string_group_dict[ordered_string].append(string)

        else:
            string_group_dict[ordered_string] = [string]

    return list(string_group_dict.values())


# better solution
# def groupAnagrams(strs):

#     ans = collections.defaultdict(list)
#     for s in strs:
#         ans[''.join(sorted(s))].append(s)
#     return ans.values()


answer = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(answer)
