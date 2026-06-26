# 1. 两数之和 (Two Sum)
# 难度：简单
# 分类：哈希
# https://leetcode.cn/problems/two-sum/

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。"""
        index_map = {}
        for index, cur in enumerate(nums):
            if target - cur in index_map:
                return [index, index_map[target - cur]]
            index_map[cur] = index


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    print(s.twoSum([3, 2, 4], 6))
