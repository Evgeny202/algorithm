def number(n):
    match = 0  # сюда будем записывать количество матчей.
    while n > 1: # создем цикл.
        if n % 2 == 0:  # проверяем четность команд.
            match += (n // 2)  # сколько было сыгранно матчей  и добавляем в match.
            n = n // 2  # сколько команд дальше прошло и плюс одна команда которая прошла автоматом.
        else:
            match += n / 2  # узнаем сколько бысо сыграно матчей и добавляем в match.
            n = n / 2  # Узнаем сколько команд осталось.
    return int(match)

print(number(7))


