class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        r = k - 1
        sb = list(s)

        while l < len(sb):
            r = l + k - 1

            if r >= len(sb):
                r = len(sb) - 1
            st = l
            # if len(sb) <
            while l < r:
                sb[l], sb[r] = sb[r], sb[l]
                l += 1
                r -= 1

            l = st + 2*k
           
        return "".join(sb)