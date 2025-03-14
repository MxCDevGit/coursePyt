# Пример 1
def task_1(A):
    summ = 0
    for i in A:
        if i > 0:
            summ += i
    return summ


# Пример 2
def task_2(A):
    summ = 0
    for i in A:
        summ += i
    return summ / len(A)


# Пример 3
def task_3(A):
    summ = 0
    sq = 0
    for i in A:
        summ += i
    avg = summ / len(A)

    for i in A:
        sq += (avg - i) ** 2

    return  (sq / len(A)) ** (1/2)
