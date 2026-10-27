class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            index = ord(task) - ord('A')
            freq[index] += 1

        max_freq = max(freq)

        max_count = 0
        for count in freq:
            if count == max_freq:
                max_count += 1

        frame = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), frame)