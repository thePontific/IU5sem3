from random import randint
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
pl=[]
def gen_random(num_count, begin, end):
    if num_count > 0:
        a = randint(begin, end)
        pl.append(a)
        gen_random(num_count - 1, begin, end)

num_count, begin, end = map(int, input("Введите количество, минимум и максимум через пробел: ").split())

gen_random(num_count, begin, end)
print(pl)