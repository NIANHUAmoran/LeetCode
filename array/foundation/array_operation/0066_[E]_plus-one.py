class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1): # 起始值(包含)，终止值(不包含)，步长
            if digits[i] != 9:
                digits[i] += 1
                return digits # 跳出for循环
            digits[i] = 0
        digits.insert(0, 1)  # 处理全部是 9 的情况
        return digits

# 测试用例
if __name__ == "__main__": # 判断当前模块是直接运行还是被导入
    solution = Solution() # 类的实例化
    print(solution.plusOne([1, 2, 9]))
    print(solution.plusOne([9, 9]))
    print(solution.plusOne([0]))