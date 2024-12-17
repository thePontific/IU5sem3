class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set() #встреченные элементы храним туут
        self.iterator = iter(items)
    def __iter__(self): #чтоб вернуть итератором для циклов
        return self
    def __next__(self):
        while True: #смотрим на элемент след. проверка есть ли в self.seen сли нет то добавляем
            item = next(self.iterator)
            check_item = item.lower() if self.ignore_case and isinstance(item, str) else item
            if check_item not in self.seen:
                self.seen.add(check_item)
                return item
if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item)

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))  # ['a', 'A', 'b', 'B']
    print(list(Unique(data, ignore_case=True)))  # ['a', 'b']
#итератор типа место где находится элемент