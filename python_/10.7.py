from pathlib import Path
path= Path('higaa.txt')

path= Path('higaa.txt')






while True:
    try:
        n = input("нажмие entor(или для выхода q)")
        if n == 'q' or n == 'Q' :
            break
        a = int(input("введите число"))
        c = input("+ , -, *, /")  
        b = int(input("введите число "))   


           
    except ValueError:  
        pass
    try:

        if c == "+":
            d = a + b
        elif c == "-":
            d = a - b
        elif c == "*":
            d = a * b
        elif c == "/":
            if b == 0:
                print("на ноль не делится ")
                pass
            d = a / b
    except NameError:
        pass     
try:
        with open("higaa.txt", "a", encoding="utf-8") as f:
            f.write(f"{a} {c} {b} = {d}\n")
        print(d)
except NameError:
    pass









