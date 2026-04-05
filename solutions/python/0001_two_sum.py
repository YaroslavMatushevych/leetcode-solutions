"""
#1 Two Sum — Easy
https://leetcode.com/problems/two-sum/

Approach: Hash Map
Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}  # {value: index}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
