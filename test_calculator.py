import unittest
from Calculator import calculate_science 


class TestCalculator(unittest.TestCase):
    def test_calculate_science(self):
        # 测试calculate_science函数的功能

        # 测试综合加法、减法、乘法和除法
        result = calculate_science(0, '2+2-3x4÷2', 0)
        self.assertEqual(result[0], -2)

        # 测试带有括号的表达式
        result = calculate_science(0, '(2+(3*4))%8*2^2', 0)
        self.assertEqual(result[0], 24)

        # 测试科学计算函数 - 正弦值、平方根、自然对数综合
        result = calculate_science(0, 'sin(45)+sqrt(16)-ln(e)+cos(45)+tan(45)', 0)
        self.assertAlmostEqual(result[0], 5.4142, places=4)

        # 测试科学计算函数 asin,acos,atan,atan
        result = calculate_science(0, 'asin(0.5)+acos(0.5)+atan(1)', 0)
        self.assertAlmostEqual(result[0], 2.35619, places=4)

        # 测试科学计算函数 log,
        result = calculate_science(0, 'log(10)', 0)
        self.assertAlmostEqual(result[0], 1, places=4)

        # 测试科学计算函数 - 阶乘
        result = calculate_science(0, '1+5!', 0)
        self.assertEqual(result[0], 121)

        # 测试阶乘嵌套括号
        result = calculate_science(0, '2+(3*(4-1)!)', 0)
        self.assertEqual(result[0], 20)

        # 测试科学计算函数 - 正弦值嵌套平方根
        result = calculate_science(0, 'sqrt(sin(45))', 0)
        self.assertAlmostEqual(result[0], 0.8409, places=4)

        # 测试科学计算函数 - 对数嵌套阶乘
        result = calculate_science(0, 'ln(5!)*π', 0)
        self.assertAlmostEqual(result[0], 15.0403, places=4)
        
        # 测试正弦值嵌套阶乘
        result = calculate_science(0, 'sqrt(sin(5!))', 0)
        self.assertAlmostEqual(result[0], 0.9306, places=4)


# if __name__ == '__main__':
#     # unittest.main()
