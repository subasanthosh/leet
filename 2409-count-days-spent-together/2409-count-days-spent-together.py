class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        prefix = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def day_of_year(date: str) -> int:
            m = int(date[:2])
            d = int(date[3:])
            return prefix[m - 1] + d

        a_start = day_of_year(arriveAlice)
        a_end = day_of_year(leaveAlice)
        b_start = day_of_year(arriveBob)
        b_end = day_of_year(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)