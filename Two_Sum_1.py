class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Constraints:

        2 <= nums.length <= 104 >> RunTime error , over 10^8 
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        
        # fist access , Brute force 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]

        # second access , Two Pointer l ,r , Sort 
        nums2 = sorted(nums)
        l,r = 0,len(nums)-1
        while(l<r):

            if nums2[l]+nums2[r] < target:
                l += 1
            elif nums2[l]+nums2[r] > target:
                r -= 1
            #break point
            elif nums2[l]+nums2[r] == target:
                return [nums.index(nums2[l]) , nums.index(nums2[r])]
            
        """

nums = [3,3]
target = 6

print(Solution.twoSum(nums,target))