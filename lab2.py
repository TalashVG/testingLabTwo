from __future__ import print_function


class One:
    """
    Class One: призначений для введення чисел типу даних float в діапазоні від 0.020 до 78.286 та обрахунку їх за
    певними формулами.Клас використовує дескриптори getter та setter для того щоб передбачити обробку виключних
    випадків, коли введені користувачем дані будуть більшими або меншими за потрібні. Також при введені не того типу
    даних в класі передбачена обробка такого виключення.

    :formula_one - повертає обраховане число за такою формулою:
        y=x^4*2.514+x^3*4.712-x^2*4.59+x*3.66
    :formula_two - повертає обраховане число за такою формулою:
        y=x^3*5.372-x^2*2.298+x*2.494
    :formula_three - повертає обраховане число за такою формулою:
        y=x^2*2.528+x*3.393
    :formula_four - повертає обраховане число за такою формулою:
        y=x*2.781
    """
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0.020:
            print("\033[91mERR. Your input is less than needed.", end=" ")
            raise Warning
        elif x > 78.286:
            print("\033[91mERR. Your input is bigger than needed.", end=" ")
            raise Warning
        else:
            self.__x = x

    def formula_one(self):
        y = self.x ** 4 * 2.514 + self.x ** 3 * 4.712 - self.x ** 2 * 4.59 + self.x * 3.66
        return y

    def formula_two(self):
        y = self.x ** 3 * 5.372 - self.x ** 2 * 2.298 + self.x * 2.494
        return y

    def formula_three(self):
        y = self.x ** 2 * 2.528 + self.x * 3.393
        return y

    def formula_four(self):
        y = self.x*2.781
        return y

#
# def main():
#     while True:
#         try:
#             x = float(input("Enter number!>>> "))
#             o = One(x)
#             break
#         except Warning:
#             print("\033[91mInput correct range!\033[0m")
#     while True:
#         try:
#             choose = int(input("Choose formula:\n1. y=x^4*2.514+x^3*4.712-x^2*4.59+x*3.66\n"
#                                "2. y=x^3*5.372-x^2*2.298+x*2.494\n"
#                                "3. y=x^2*2.528+x*3.393\n"
#                                "4. y=x*2.781\n>>> "))
#             if choose == 1:
#                 print("y = {}".format(o.formula_one()))
#                 break
#             elif choose == 2:
#                 print("y = {}".format(o.formula_two()))
#                 break
#             elif choose == 3:
#                 print("y = {}".format(o.formula_three()))
#                 break
#             elif choose == 4:
#                 print("y = {}".format(o.formula_four()))
#                 break
#             else:
#                 print("\033[91mERR. You entered wrong choose, try again!\033[0m")
#
#         except ValueError:
#             print("\033[91mERR. You entered wrong choose, try again!\033[0m")
#
#
# if __name__ == '__main__':
#     while True:
#         main()
#         e = input("if you want to interrupt press some key, else press Enter ")
#         if e == "":
#             continue
#         else:
#             break
#
