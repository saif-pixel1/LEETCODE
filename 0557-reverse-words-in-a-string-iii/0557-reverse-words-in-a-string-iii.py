class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0 
        r = 0
        sb = list(s)
        
        for i in range(len(sb)):
            if sb[i] != " ":
                i+=1
            else:
                r = i-1
                while l<r:
                    sb[l],sb[r] = sb[r], sb[l]
                    l+=1
                    r-=1
                l= i + 1
        r =len(sb)-1
        while l<r:
            sb[l],sb[r] = sb[r], sb[l]
            l+=1
            r-=1

        return "".join(sb)
                

            



        