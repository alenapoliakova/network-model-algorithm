# Расчет временных характеристик сетевых моделей
Алгоритм для подсчёта временных характеристик сетевых моделей. С помощью сетевой модели 
моделируется процесс производства изделия. Для подсчёта используется алгоритм с тактами.  

Моя статья про алгоритм: https://habr.com/ru/articles/739368/

## Результирующая таблица содержит данные:
- `i` - номер работы
- `t(i)` - время выполнения работы
- `K(i)` - множество работ, предшествующих работе с номером `i`
- `t(rn, i)` - время самого _раннего начала_ выполнения работы с номером `i`
- `t(rk, i)` - время самого _раннего окончания_ выполнения работы с номером `i`
- `t(pn, i)` - время самого _позднего начала_ выполнения работы с номером `i`
- `t(pk, i)` - время самого _позднего окончания_ выполнения работы с номером `i`
- `r(i)` - резерв времени работы с номером `i` (время, на которое не в ущерб времени общего окончания 
выполнения всех работ, можно задерживать выполнение работы с номером `i`)

## Использование:
1. Установите библиотеку для отображения данных в таблице:  
`pip install prettytable`
2. Запустите программу:  
`python network_model_algorithm.py`
3. Введите исходные данные: количество работ, для каждой из работ время её выполнения и множество 
работ, предшествующих ей (через запятую, либо через enter, если нет предшествующих работ).
4. Значение строки конечной работы столбца `t(rk, i)` будет длиной критического пути 
(временем выполнения всех работ для изготовления изделий).

## Пример результирующей таблицы:
![img.png](img.png)  
