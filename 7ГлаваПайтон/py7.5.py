while True:
    n = int(input("сколько вам лет?"))
    if n == 'q' or n == 'Q' :
        break
    else:
        if n <= 3 :
            print("билет бесплатный")
        elif n<=12 :
            print("стоимость билета 10 долларов")
        else:
            print("стоимость билета 15 долларов")         