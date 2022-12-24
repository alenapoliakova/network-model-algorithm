from collections import namedtuple
from prettytable import PrettyTable

input_model = namedtuple("input_model", ["time", "set_k"])
row = namedtuple("row", ["i", "time", "set_k", "rn", "rk", "pn", "pk", "r"])


def search_next_numbers(node: int) -> set[int]:
    numbers = set()
    for number, model in models.items():
        if node in model.set_k:
            numbers.add(number)
    if not numbers:
        return set()
    next_numbers = set()
    for num in numbers:
        next_numbers.update(search_next_numbers(num))
    next_numbers.update(numbers)
    next_numbers.discard(node)
    return next_numbers


def print_table(data: dict[int, row]):
    pretty_table = PrettyTable()

    pretty_table.field_names = ["i", "t(i)", "K(i)", "t(rn, i)", "t(rk, i)", "t(pn, i)", "t(pk, i)", "r(i)"]

    for line in data.values():
        pretty_set = line.set_k if len(line.set_k) > 0 else "{}"
        pretty_table.add_row([line.i, line.time, pretty_set, line.rn, line.rk, line.pn, line.pk, line.r])

    print(pretty_table)


n = int(input("Введите количество работ="))
models: dict[int, input_model] = dict()

for i in range(1, n + 1):
    time = int(input(f"Введите время t({i})="))
    raw_k = input(f"Введите через пробел множество K({i})=")
    set_k = set(map(lambda data: int(data), raw_k.split()))
    models[i] = input_model(time=time, set_k=set_k)

table: dict[int, row] = dict()

for number, model in models.items():
    time = model.time
    set_k = model.set_k
    if len(set_k) == 0:
        rn = 1
    else:
        rn = max([table[s].rk for s in set_k]) + 1
    rk = rn + model.time - 1
    table[number] = row(i=number, time=time, set_k=set_k, rn=rn, rk=rk, pn=None, pk=None, r=None)

for number, model in list(models.items())[::-1]:
    visited = search_next_numbers(number)
    current_row = table[number]
    if visited:
        k = min(visited, key=lambda num: table[num].pn if table[num].pn is not None else 10000000000)
        pk = table[k].pn - 1
    else:
        pk = current_row.rk
    pn = pk - current_row.time + 1
    r = pn - current_row.rn
    assert r == pk - current_row.rk and r >= 0, print(f"{current_row}, r={r}, {pk - current_row.rk}")
    table[number] = table[number]._replace(pk=pk, pn=pn, r=r)

print_table(table)
