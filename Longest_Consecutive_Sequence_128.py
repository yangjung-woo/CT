# 128. Longest Consecutive Sequence

# You must write an algorithm that runs in O(n) time.

# 가장 긴 연속된 수열의 길이를 반환하는 문제 
'''
    Constraints:

    0 <= nums.length <= 105     * 시간복잡도 O(n)이하로 해결해야함 
                                * nums = [] 인 경우도 고려
                                * nums [0 0 0 ], 중복값이 들어간 경우도 고려 
    -109 <= nums[i] <= 109

'''

class Solution(object):
    def longestConsecutive( nums):
        # sort의 시간복잡도 = O(nlogn)
        longest = 0
        nums.sort()
        nums_dict ={} # O(n)
        for n in nums:
            nums_dict[n] = True

        for cur_num in nums_dict:
            prev = cur_num-1
            if prev not in nums_dict:
                cnt=1
                target = cur_num + 1
                while target in nums_dict:
                    target +=1
                    cnt+=1
                longest = max(longest,cnt)
        return longest





print(Solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
        