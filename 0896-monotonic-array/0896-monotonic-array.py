class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        l = 0 ; r = len(nums) - 1

        # while l<r:
        #     if nums[l] > nums[r]:
        #         # dec
        #         # l+=1
        #         for i in range(r):
        #             if nums[i+1] > nums[i]:
        #                 return False
        #     else:
        #         # r-=1
        #         # in
        #         # if nums[r] < nums[r-1]:
        #         #     return False
        #         for i in range(r-1, -1,-1):
        #             if nums[i] < nums[i-1]:
        #                 return False
        #     l+=1
        #     r-=1
        # return True



        l = 1 ; inc = True ; dec = True
        while l<len(nums):
            if nums[l] > nums[l-1]:
                inc = False
            if nums[l] < nums[l-1]:
                dec= False
            l+=1
        return inc|dec
                    

            
        
        