class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        conteiner = 0       # создали счетчик для прибыли
        for i in range(1, len(prices)): #проходимся по всем элементам в списке начиная с 1 индекса т.к с 0 неимеет смысла
            if prices[i] - prices[i - 1] > 0:   # возмем список [7,1,5,3,6,4] к  примеру если из 5-1 = 4, то 4 добавляем в счетчик, если 3-5 = -2, то не добавляем т.к это будет нам в убыток.
                conteiner += prices[i] - prices[i - 1]
        return conteiner #возращаем контейнер с максимальной прибылью без потерь.