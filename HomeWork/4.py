def sumBase(n, k):
    number = 0  # Создаю список куда будет
    while n != 0:
        number += n % k  # к списку прибовляю остаток от деления на цело
        n = n // k  # n равно челой части  от деления n на k
    return number  # возращаю number

print(sumBase(43, 6))
