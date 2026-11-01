class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        arr = s.split()
        l=0;r=len(arr)-1
        while l<r:
            arr[l], arr[r]=arr[r], arr[l]
            l+=1
            r-=1
        return " ".join(arr)




        