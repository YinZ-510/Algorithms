# 只出现一次的数字
# https://leetcode-cn.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num = set(nums)
        sum1 = sum(nums)
        sum2 = sum(num)
        return sum2*2 - sum1

        '''
        将所有数字进行异或操作即可。对于异或操作明确以下三点：
            一个整数与自己异或的结果是0
            一个整数与0异或的结果是自己
            异或操作满足交换律，即a^b=b^a
        '''
        '''
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res
        '''
        
