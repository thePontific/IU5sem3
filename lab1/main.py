import sys
import math

def get_coefficient(name):
    while True:
        try:
            value = input(f"Введите коэффициент {name}: ")
            return float(value)
        except ValueError:
            print(f"Ошибка: коэффициент {name} должен быть числом. Попробуйте снова.")

def korni(t, otvet):
    if t < 0:
        print(f"Действительных корней нет для t = {t}")
        return
    x1 = math.sqrt(t)
    otvet.add(x1)
    otvet.add(-x1)

def reshenie(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен 0 для биквадратного уравнения.")
        return []

    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * a * c
    print(f"Дискриминант: {discriminant}")
    if discriminant < 0:
        print("Дискриминант меньше 0. Действительных корней нет.")
        return []
    else:
        otvet = set()
        sqrt_d = math.sqrt(discriminant)
        t1 = (-b + sqrt_d) / (2 * a)
        t2 = (-b - sqrt_d) / (2 * a)
        print(f"t1 = {t1}, t2 = {t2}")
        korni(t1, otvet)
        korni(t2, otvet)

    return sorted(otvet)

def main():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Ошибка: один или несколько коэффициентов некорректны. Вводите вручную.")
            a = get_coefficient('A')
            b = get_coefficient('B')
            c = get_coefficient('C')
    else:
        print("Введите коэффициенты для уравнения Ax^4 + Bx^2 + C = 0")
        a = get_coefficient('A')
        b = get_coefficient('B')
        c = get_coefficient('C')

    otvet = reshenie(a, b, c)

    if otvet:
        print("Действительные корни уравнения:", otvet)
    else:
        print("Корней нет.")

if __name__ == "__main__":
    main()
