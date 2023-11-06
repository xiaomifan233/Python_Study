class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = {}
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted(diff.keys())
        j = s = 0
        for p, i in sorted(zip(people, range(len(people)))):
            while j < len(times) and times[j] <= p:
                s += diff[times[j]]  # 累加不超过 people[i] 的差分值
                j += 1
            people[i] = s  # 从而得到这个时刻花的数量
        print(people)