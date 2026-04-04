oneS = ['тунец', 'ананас', 'ветчина']
tweS = []
while True :
    print(oneS)
    v = input("какую начинку какую начинку добавить в бургер ?")
    oneS.remove(v)
    tweS.append(v)
    print(f"я приготовил вам бургер с начинкой: {tweS}")
    e = input("хотите добавить еще начинку ? да/нет")
    if e == 'нет':
        break 
