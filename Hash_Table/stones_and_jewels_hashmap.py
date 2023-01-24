

import collections


def numJewelsInStones(jewels, stones):

    jewel_map = {}
    # create your jewl counter hashmap

    for jewl in jewels:
        jewel_map[jewl] = 0

    for stone in stones:
        if stone in jewel_map:
            jewel_map[stone] += 1

    return sum(list(jewel_map.values()))


answer = numJewelsInStones("sad", "SaaaaDd")
print(answer)


#(list(map(lambda x: x + 1, [1, 2, 3])))
