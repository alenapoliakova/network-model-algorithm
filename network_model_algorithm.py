from collections import namedtuple
from prettytable import PrettyTable

input_model = namedtuple("input_model", ["time", "set_k"])
row = namedtuple("row", ["i", "time", "set_k", "rn", "rk", "pn", "pk", "r"])


def search_next_numbers(work_idx: int) -> set[int]:
    """Поиск следующих номеров работ, которые зависят от данной."""
    next_nums = {idx for idx, model in models.items()
                 if work_idx in model.set_k and idx != work_idx}  # Проверка на цикличность
    for next_num in next_nums.copy():
        next_nums.update(search_next_numbers(next_num))
    next_nums.discard(work_idx)
    return next_nums


def print_table(data: dict[int, row]) -> None:
    """Вывод таблицы с подсчитанными данными для сетевой модели в консоль."""
    pretty_table = PrettyTable()
    pretty_table.field_names = ["i", "t(i)", "K(i)", "t(rn, i)", "t(rk, i)", "t(pn, i)",
                                "t(pk, i)", "r(i)"]
    for line in data.values():
        pretty_set = line.set_k if len(line.set_k) > 0 else "{}"
        pretty_table.add_row(
            [line.i, line.time, pretty_set, line.rn, line.rk, line.pn, line.pk, line.r]
        )
    print(pretty_table)


amount = int(input("Введите количество работ="))
models: dict[int, input_model] = {}

for idx in range(1, amount + 1):
    time = int(input(f"Введите время t({idx})="))
    raw_k = input(f"Введите через пробел множество K({idx})=")
    set_k = set(map(lambda data: int(data), raw_k.split()))
    models[idx] = input_model(time=time, set_k=set_k)

table: dict[int, row] = dict()

for idx, model in models.items():
    if not model.set_k - {idx}:
        rn = 1
    else:
        rn = max(table[last_idx].rk for last_idx in model.set_k if last_idx != idx) + 1
    rk = rn + model.time - 1
    table[idx] = row(i=idx, time=model.time, set_k=model.set_k, rn=rn, rk=rk,
                     pn=None, pk=None, r=None)

for idx, model in list(models.items())[::-1]:
    visited = search_next_numbers(idx)
    current_row = table[idx]
    if visited:
        pk = min(num for visit in visited if (num := table[visit].pn) is not None) - 1
    else:
        pk = current_row.rk
    pn = pk - current_row.time + 1
    r = pn - current_row.rn
    if r != pk - current_row.rk or r < 0:
        raise ValueError(f"Невозможно построить модель для работы {idx}")
    table[idx] = table[idx]._replace(pk=pk, pn=pn, r=r)

print_table(table)
