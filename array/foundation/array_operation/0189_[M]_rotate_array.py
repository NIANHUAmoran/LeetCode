# -*- coding: utf-8 -*-
# @Time : 2025/4/17 14:55
# @Author : Chuanwei Zhang
# @Email : 2722419346@qq.com
# @File : 0189_[M]_rotate_array.py
# @Project : LeetCode

# 个人方案，时间复杂度太高
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 处理k大于数组长度的情况

        for _ in range(k):
            # 保存最后一个元素
            last = nums[-1]

            # 所有元素向后移动一位（从后往前操作避免覆盖）
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            # 把原最后一个元素放到第一位
            nums[0] = last
        return nums


if __name__ == "__main__": # 判断当前模块是直接运行还是被导入
    solution = Solution() # 类的实例化
    print(solution.rotate([1,4,6,8,3],8))