import collections


# 2. Считалочка Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
# Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
# Игра происходит до тех пор, пока не останется последний человек.
# Для данных N и К дать номер последнего оставшегося человека.

def counting(n: int, k: int):
    """
    Функция реализует детскую считалку. Вычисляет последнего оставшегося человека.
    :param n: Количество человек
    :param k: Количество слогов в считалочке
    :return: Номер оставшегося чеорвека
    """

    q = [i for i in range(1, n + 1)]
    i = 0

    if n < 1:
        return None
    elif n == 1:
        return n

    while n > k:
        i += k - 1
        if i >= n:
            i -= n
        q.pop(i)
        n -= 1

    while n > 1:
        i += k % n - 1
        if i >= n:
            i -= n
        q.pop(i)
        if i == -1:
            i = 0
        n -= 1

    return q

# 4. Навигатор на сетке.
#    Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
#    Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.

def dijkstra(roster, start, finish):
    length = len(roster)
    width = len(roster[0])
    cells = [(i, j) for i in range(length) for j in range(width)]
    hist = {}
    costs = {cell: roster[cell[0]][cell[1]] for cell in cells}
    res = {cell: ('', float('inf')) for cell in cells}
    res[start] = ('', 0)
    queue = [(start, 0), ]
    while queue:
        target = queue.pop(0)
        if hist.get(target[0]) is None:
            hist[target[0]] = ''
        next_cells = []
        if start[0] - 1 >= 0:
            next_cells.append((start[0] - 1, start[1]))
        if start[0] + 1 < length:
            next_cells.append((start[0] + 1, start[1]))
        if start[1] - 1 >= 0:
            next_cells.append((start[0], start[1] - 1))
        if start[1] + 1 < width:
            next_cells.append((start[0], start[1] + 1))
        for cell in next_cells:
            parent_cost = (target[0], costs[(target[0], cell)])
            if parent_cost[1] + target[1] < res[cell][1]:
                res[cell] = (parent_cost[0], parent_cost[1] + target[1])
                queue.append((cell, parent_cost[1] + target[1]))

    return res[finish]

# 6. Аренда ракет
# Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на
# использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

def sum_time(queue: list) -> bool:
    """
    Функция проверяет возможность удовлетворения ВСЕХ поданных заявок - сравнивает время окончания каждой
    с временем начала следующей.
    :param queue: список заявок
    :return: bool
    """
    queue.sort()
    for i in range(len(queue) - 1):
        if queue[i][1] > queue[i + 1][0]:
            return False
    return True

# 7. Сорт
# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом

def count_sort(block: list) -> list:
    """
    Функция реализует сортировку  подсчетом
    :param block: Исходный список
    :return: Отсортированный список
    """
    count_buffer = collections.defaultdict(int)
    res = []
    for elem in block:
        count_buffer[elem] += 1
    for num in range(13, 26):
        res.extend([num, ] * count_buffer[num])
    return res



if __name__ == '__main__':
    print(counting(5, 2))
    print(counting(5, 4))
    print(counting(5, 6))
    print(counting(5, 7))
