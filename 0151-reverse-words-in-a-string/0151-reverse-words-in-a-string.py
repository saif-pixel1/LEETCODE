class Solution:
    def reverseWords(self, s: str) -> str:
        # trim 
        # reverse the whole str 
        l=0;r=len(s)-1
        while l<=r:
            if s[l] == " ":
                l+=1
            elif s[r] == " ":
                r-=1
            else:
                break
        sb = ""
        while l<=r:
            if s[l] != " ":
                sb += s[l]
                l+=1
            elif s[l] == " ":
                if s[l-1] !=" ":
                    sb+=s[l]
                    l+=1
                else:
                    l+=1

        arr = list(sb)
        i =0 ; j=len(sb)-1

        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1

        m=0;n=0
        while m<len(arr):
            while n<len(sb) and arr[n]!=" ":
                n+=1

            p1,p2 = m,n-1
            while p1<p2:
                arr[p1],arr[p2] = arr[p2],arr[p1]
                p1+=1
                p2-=1
            m=n+1
            n=m
        return "".join(arr)
                


            

            
        