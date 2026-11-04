class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0 
        r =0
        sb = []

        while l<len(word1) and r<len(word2):
            sb.append(word1[l])
            sb.append(word2[r])

            l+=1
            r+=1
        while l<len(word1):
            sb.append(word1[l])
            l+=1
        while r<len(word2):
            sb.append(word2[r])
            r+=1
        return "".join(sb)

              




# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         l = 0
#         r = len(word1)
#         word = list(word1 + word2)

#         while l < len(word1) and r < len(word):
#             word[l + 1], word[r] = word[r], word[l + 1]
#             l += 1

#             if l==1:
#                 word[l+1], word[r] = word[r], word[l+1]
#                 r+=1
#             else:
#                 r+=1

#             # if l % 2 == 0:
#             #     r += 1
#         return "".join(word)