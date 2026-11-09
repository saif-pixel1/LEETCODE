class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l = 0 
        c = 0
        arr = []
        while l<len(s1):
            if s1[l] != s2[l]:
                arr.append(l)
                c+=1
                l+=1
            else:
                l+=1
        if c==2:
            i = arr[0]
            j = arr[1]
            if s1[i] != s2[j] or s1[j] != s2[i]:
                return False
            return True
        elif c==0:
            return True
        return False
        


        