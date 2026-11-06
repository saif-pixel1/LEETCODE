class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        for i in words:
            l = 0
            r = len(i)-1
            while l<r:
                if i[l] == i[r]:
                    l+=1
                    r-=1
                else:
                    break
            if l>=r:
                return i    
        return "" 

                
            