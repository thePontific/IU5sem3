def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(func.__name__)

        if isinstance(result, list): #выводим каждый элемент списка
            for item in result:
                print(item)
        elif isinstance(result, dict):# словарик ключ=знач
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result) #все остальное как есть выводим
        return result
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
