class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l = 0 
        r = len(s)-1
        if s == "":
            return 0
        while l<r:
            if s[l]!=s[r]:
                return 2
            l+=1
            r-=1
        return 1
            


        
        