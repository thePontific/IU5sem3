data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    def abs_key(x):
        return abs(x)
    result = sorted(data, key=abs_key, reverse=True)
    print(result)


    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
#key — правило сортировки.
#lambda x: abs(x) —берем x из списка и возвращаем (abs(x)).
