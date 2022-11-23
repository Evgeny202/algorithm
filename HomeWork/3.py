def numJewelsInStones(stones, jewels):
    stone = 0  # создаю список куда буду ложить все найденные драгоценные камни.
    for i in jewels:  # Прохожу по драгоценным камням.
        for j in stones:  # Также прохожу по обычным камням с драгоценными.
            if i == j:  # Нахожу есть ли совпадение.
                stone += 1  # Добавляю найденный драгоценный камень в список.
    return stone  # возращаю список с количеством драгоценных камней

print(numJewelsInStones('aA', 'aAAbbbb'))