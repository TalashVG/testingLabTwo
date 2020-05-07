from lab2 import One
import unittest


class TestOne(unittest.TestCase):

    def testCaseOne(self):
        # Введення цілого додатнього числа яке не входить до діапазону
        # Passed
        with self.assertRaises(Warning):
            One(-100)

    def testCaseTwo(self):
        # Введення знаку табуляції перед числом
        # Passed
        self.assertEquals(One(int("   40")).x, 40)

    def testCaseThree(self):
        # Введення знаку табуляції після числа
        # Passed
        self.assertEquals(One(int("40   ")).x, 40)

    def testCaseFour(self):
        # Введення в числі знаку табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(int(" 4   0 "))

    def testCaseFive(self):
        # Введення цілого від'ємного числа
        # Passed
        with self.assertRaises(Warning):
            One(-30)

    def testCaseSix(self):
        # Введення цілого від'ємного числа з табуляцією
        # Passed
        with self.assertRaises(ValueError):
            One(int("-  30"))

    def testCaseSeven(self):
        # Введення цілого від'ємного числа з табуляцією
        # Passed
        with self.assertRaises(Warning):
            One(int("   -30"))

    def testCaseEight(self):
        # Введення цілого двохзначного від'ємного числа з символом табуляції чи пробілу
        # Passed
        with self.assertRaises(ValueError):
            One(int("- 3 0"))

    def testCaseNine(self):
        # Введення дробового числа з крапкою
        # Passed
        self.assertEquals(One(2.2).x, 2.2)

    def testCaseTen(self):
        # Введення дробового числа з комою
        # Passed
        with self.assertRaises(ValueError):
            One(float("2,2"))

    def testCaseEleven(self):
        # Введення дробового від'ємного числа без десяткової частини
        # Passed
        with self.assertRaises(Warning):
            One(float("-1."))

    def testCaseTwelve(self):
        # Введення дробового додатнього числа без десяткової частини
        # Passed
        self.assertEquals(One(float(1.)).x, 1.0)

    def testCaseThirteen(self):
        # Введення дробового числа з символами табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(float("2 8 . 45 "))

    def testCaseFourteen(self):
        # Введення дробового числа без цілої частини
        # Failed
        with self.assertRaises(ValueError):
            One(float(".456"))

    def testCaseFifteen(self):
        # Введення дробового числа з крапкою та комою
        # Passed
        with self.assertRaises(ValueError):
            One(float("6.,234"))

    def testCaseSixteen(self):
        # Введення дробового числа з крапкою та комою але розділене символом табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(float("1   .,025"))

    def testCaseSeventeen(self):
        # Введення дробового числа з крапкою та комою але розділене символом табуляції поза межами допустимих значень
        # Passed
        with self.assertRaises(ValueError):
            One(float("456.,   234"))

    def testCaseEighteen(self):
        # Введення сторонього символу
        # Passed
        with self.assertRaises(ValueError):
            One(float("ggg"))

    def testCaseNineteen(self):
        # Ведення сторонього символу разом із числом
        # Passed
        with self.assertRaises(ValueError):
            One(float("11ggg"))

    def testCaseTwenty(self):
        # Ведення сторонього символу разом із числом розділених символом табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(float("11   ggg"))

    def testCaseTwentyTOne(self):
        # Ведення сторонього символу разом із числом поза межами діапазону розділених символом табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(float("7544 III"))

    def testCaseTwentyTwo(self):
        # Обчислення цілого додатнього числа поза межами діапазону
        # Passed
        with self.assertRaises(Warning):
            One(49833)

    def testCaseTwentyThree(self):
        # Обчислення цілого додатнього числа з табуляцією
        # Passed
        self.assertEquals(One(float("40   ")).formula_one(), 6730210.399999999)

    def testCaseTwentyFour(self):
        # Обчислення цілого додатнього числа з табуляцією
        # Passed
        self.assertEquals(One(float("   40")).formula_one(), 6730210.399999999)

    def testCaseTwentyFive(self):
        # Обчислення цілого двохзначного додатнього числа з символом табуляції чи пробілу
        # Passed
        with self.assertRaises(ValueError):
            One(float(" 1 23"))

    def testCaseTwentySix(self):
        # Обчислення цілого від'ємного числа
        # Passed
        with self.assertRaises(Warning):
            One(-20)

    def testCaseTwentySeven(self):
        # Обчислення цілого від'ємного числа з табуляцією
        # Passed
        with self.assertRaises(Warning):
            One(float("-20   "))

    def testCaseTwentyEight(self):
        # Обчислення цілого від'ємного числа з табуляцією
        # Passed
        with self.assertRaises(Warning):
            One(float(" -20"))

    def testCaseTwentyNine(self):
        # Обчислення цілого двохзначного від'ємного числа з символом табуляції чи пробілу
        # Passed
        with self.assertRaises(ValueError):
            One(float(" -   2  1"))

    def testCaseThirty(self):
        # Обчислення цілого двохзначного від'ємного числа з символом табуляції чи пробілу
        # Passed
        with self.assertRaises(ValueError):
            One(float(" -   2"))

    def testCaseThirtyOne(self):
        # Обчислення цілого додатнього двохзначного дробового числа в межах діапазону
        # Passed
        self.assertEquals(One(1.24).formula_one(), 12.408461680639999)

    def testCaseThirtyTwo(self):
        # Обчислення цілого додатнього двохзначного дробового числа  з табуляцією
        # Passed
        with self.assertRaises(ValueError):
            One(float("1. 24"))

    def testCaseThirtyThree(self):
        # Введення сторонього символу
        # Passed
        with self.assertRaises(ValueError):
            One(float("iiii"))

    def testCaseThirtyFour(self):
        # Ведення сторонього символу разом із числом
        # Passed
        with self.assertRaises(ValueError):
            One(float("7rR"))

    def testCaseThirtyFive(self):
        # Ведення сторонього символу разом із числом розділених символом табуляції
        # Passed
        with self.assertRaises(ValueError):
            One(float("1 kk"))
