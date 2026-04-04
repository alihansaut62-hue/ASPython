from random import randint

class Ran:
    def __init__(self):
        pass

    def colf(self, kub=6):
        i = 0  
        while True:
            i += 1
            b = i % 2

            a = randint(0, kub)
            b = randint(0, kub)
            c = randint(0, kub)
            d = randint(0, kub)

            print("Вывод:", a)
            print("Вывод:", b)
            print("Вывод:", c)
            print("Вывод:", d)
            print("Попытка №", i)
            print("------")


            if a == kub and b == kub and c == kub and d == kub:
                print("🎉 вы выбили джекпот")
                print(f"c {i} попытки выиграли")
                break
            if b == 0:
               print("красное")
            else:
               print("Черное")
            


sdf = Ran()      # создаём объект
sdf.colf(8)      # вызываем метод
