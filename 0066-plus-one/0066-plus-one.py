class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        l = 0
        while l<len(digits):
            s+= str(digits[l])
            l+=1
        re = int(s)
        r = str(re + 1 )
        l=0;arr=[]
        while l<len(r):
            arr.append(int(r[l]))
            l+=1
        return arr

        