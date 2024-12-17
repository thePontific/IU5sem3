
def field(items, *args):
    assert len(args) > 0 #обязательно верно
    for item in items:
        if len(args) == 1:
            # 1 АРГУМЕНТ = ЗНАЧЕНИЕ
            value = item.get(args[0])
            if value is not None:
                yield value #как ретурн но для генераторов, типа большой набор значений который надо прочитать 1 раз
        else:
            # НЕСКОЛЬКО АРГ=СЛОВАРЬ
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:
                yield result
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))
