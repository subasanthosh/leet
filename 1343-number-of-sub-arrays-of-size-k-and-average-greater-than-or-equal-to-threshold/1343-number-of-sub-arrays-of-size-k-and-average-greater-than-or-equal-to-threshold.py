class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        avg = 0
        for i in range(k):
            avg += arr[i]
        print(avg)
        if (avg/k)>=threshold:
            count+=1


        for i in range(len(arr)-k):
            avg = avg-arr[i]+arr[i+k]
            if (avg/k)>=threshold:
                count+=1

        return count