# 01_02_06


# PrintClassの作成とprint_meメソッド（関数の作成）
class PrintClass:
    def print_me(self):
        print(self.x, self.y)


# インスタンスの作成、生成
pl = PrintClass()

# 属性の値を代入
pl.x = 10
pl.y = 100
pl.z = 1000

# メソッドの呼び出し
pl.print_me()


class MyCalcClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_add1(self, a, b):
        return a + b

    def calc_add2(self):
        return self.x + self.y

    def calc_multi(self, a, b):
        return a * b

    def calc_print(self, a):
        print('data:{0}:yの値{1}'.format(a, self.y))


instance_1 = MyCalcClass(1, 2)
instance_2 = MyCalcClass(5, 10)
