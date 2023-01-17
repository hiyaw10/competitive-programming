class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        hashmap = Counter(deliciousness)
        count = 0

        for num in hashmap.keys():
            x = float('inf')
            if num != 0:
                x = 2**(int(math.log(num, 2)) + 1) - num
                if math.floor(math.log(num, 2)) == math.log(num,2):
                    count += hashmap.get(0, 0) * hashmap[num]

            if (x in hashmap) and (x <= num):
                if x == num:
                    count += (hashmap[num] * (hashmap[num] - 1))/2
                else:
                    count += (hashmap[num] * hashmap[x])

        return int(count) % (10**9 + 7)