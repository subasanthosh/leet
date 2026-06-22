class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        n = len(digits)
        flag = 0
        while(i<n):
            if digits[n-i-1]!=9:
                digits[n-i-1]+=1
                flag = 1
                break
            elif digits[n-i-1]==9:
                digits[n-i-1] = 0
                flag = 0
            i+=1

        if flag==0:
            digits.insert(0,1)
        return digits

                
        