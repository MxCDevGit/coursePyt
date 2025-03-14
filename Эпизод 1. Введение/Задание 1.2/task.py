import math

# Пример 1
def task_1(a, b):
    if a > b:
        answer = (a*b)**(1/2)-3
    if a == b:
        answer = math.log10(2)
    if a < b:
        answer = math.log(a**3+1)/b
    return answer


# Пример 2
def task_2(a, b):
    if a < b:
        answer = math.tan(a/b)+1
    if a == b:
        answer = math.tan(-1)
    if a > b:
        answer = ((a*b-5)**(1/2))/a
    return answer


# Пример 3
def task_3(a, b):
    if a > b:
        answer = math.log10(a*b)+21
    if a == b:
        answer = math.tan(-5)
    if a < b:
        answer = math.log(3*a/b)+1
    return answer


# Пример 4
def task_4(a, b):
    if a > b:
        answer = (a*b-1)**(1/2)
    if a == b:
        answer = math.log10(255)
    if a < b:
        answer = math.tan(a-5)/b
    return answer


# Пример 5
def task_5(a, b):
    if a > b:
        answer = math.log(a/b)+31
    if a == b:
        answer = math.tan(-25)
    if a < b:
        answer = math.cos(a*5-1)/a
    return answer


# Пример 6
def task_6(a, b):
    if a < b:
        answer = (b/a+1)**(1/2)
    if a == b:
        answer = 25**(1/2)
    if a > b:
        answer = math.log10(a**3-5)/b
    return answer
