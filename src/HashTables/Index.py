from collections import deque


def two_sum(input=[2, 7, 11, 15], target=9):

    hash_map = {}

    for i in range(len(input)):
        result = target - input[i]
        if result in hash_map:
            return [hash_map[result], i]
        hash_map[input[i]] = i
    return result[hash_map]

# print(two_sum())


# 217. Contains Duplicate
def contains_duplicates(input=[1, 2, 3, 1]):

    _map = {}
    for i in input:
        if i in _map:
            return True
        _map[i] = 1

    return False

# print(contains_duplicates())


# 169. Majority Element
def majority_element(input=[3, 2, 3]):

    m = {}

    for i in input:
        m[i] = m.get(i, 0) + 1
    for i in input:
        if m[i] > len(input) // 2:
            return i

# print(majority_element())

# 49. Group Anagrams


class Solution:

    def find_hashed(self, s):
        return ''.join(sorted(s))

    def group_anagram(self, input=["eat", "tea", "tan", "ate", "nat", "bat"]):

        m = {}
        ans = []

        for s in input:
            hashed = self.find_hashed(s)

            if hashed not in m:
                m[hashed] = []
            m[hashed].append(s)

        for v in m.values():
            ans.append(v)

        return ans

    # print()


# 454. 4Sum II
def four_sum_count(a=[1, 2], b=[-2, -1], c=[-1, 2], d=[0, 2]):

    m = {}
    ans = 0

    sec_a = len(a)
    sec_b = len(b)
    sec_c = len(c)
    sec_d = len(d)

    for i in range(0, sec_a):
        x = a[i]

        for j in range(0, sec_b):
            y = b[j]

            if x + y not in m:
                m[x + y] = 0
            m[x + y] += 1

    for i in range(0, sec_c):
        x = c[i]

        for j in range(0, sec_d):
            y = d[j]
            target = - (x + y)

            if target in m:
                ans += m[target]

    return ans

# print(four_sum_count())


# 146. LRU Cache


class LRUCache:
    def __init__(self, capacity):
        self.c = capacity
        self.m = dict()
        self.diq = deque()

    def get(self, key):
        if self.key in m:
            value = self.m[key]
            self.diq.remove(key)
            self.diq.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key not in m:
            if len(self.diq) == self.c:
                oldest = self.diq.popleft()
                del self.m[oldest]
        else:
            return self.remove(key)

        self.m[key] = value
        self.diq.append(key)
        
        
    # def __init__(self, capacity: int):
    #     self.cache_size = capacity
    #     self.cache_maps = {}

    # def get(self, key: int) -> int: # O(1)
    #     if key in self.cache_maps: # O(1)
    #         value = self.cache_maps[key]
    #         self.cache_maps.pop(key) # O(1)
    #         self.cache_maps[key] = value
    #         return value
    #     return -1

    # def put(self, key: int, value: int) -> None: # O(1)
    #     if key in self.cache_maps: # O(1)
    #         self.cache_maps.pop(key) # O(1)
    #     elif len(self.cache_maps) == self.cache_size:
    #         self.cache_maps.pop( next(iter(self.cache_maps)) ) # O(1)
    #     self.cache_maps[key] = value
