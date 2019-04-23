# coding=utf-8
class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.current_v = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.current_v + v <= self.capacity

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.current_v += v


b = MoneyBox(3)
print(b.can_add(1))
print(b.can_add(3))
print(b.can_add(4))
b.add(2)
print(b.can_add(1))
print(b.can_add(3))
