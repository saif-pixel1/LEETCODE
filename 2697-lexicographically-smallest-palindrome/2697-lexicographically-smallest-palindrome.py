class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        sb = list(s)
        l = 0
        r = len(sb)-1
        
        while l<r:
            if sb[l] != sb[r]:
                if sb[l]<sb[r]:
                    sb[r] = sb[l]
                else:
                    sb[l] = sb[r]
                l+=1
                r-=1
            else:

                l+=1
                r-=1
        return "".join(sb)
        

        