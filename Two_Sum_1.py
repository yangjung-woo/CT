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

        # second access , Two Pointer l ,r , Sort  ,wrong 동일한  값이 들어오면 오류 발생
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

        # third access , dictionary 사용 
        
            


        # best Solution 딕셔너리는 key search에 소요시간은 단 O(1) 이다 
        
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
        """

        '''
        origin_indices = {} # dictionary

        for idx, val in enumerate(nums):
            if val in origin_indices:
                origin_indices[val].append(idx)
            else:
                origin_indices[val] = [idx]

        nums.sort()

        l, r = 0, len(nums)-1 # two pointer apply 

        while l < r:
            if target > (nums[l] + nums[r]):
                l += 1
            elif target < (nums[l] + nums[r]):
                r -= 1
            else:
                return [origin_indices[nums[l]][0], origin_indices[nums[r]][-1]] # 정답은 단 1개이기에 달성시 종료 
            
        '''

        # 해시테이블 

nums = [3,0,5,8,1,6,7]
target = 6

print(Solution.twoSum(nums,target))