from pathlib import Path
path = Path(r'C:\Users\Admin\Desktop\python_\experiments\sdfg')
pat = Path('text')
run = path.read_text()
run = run.rstrip()
ru = pat.read_text()
ru = ru.rstrip()
print(run)
print(ru)













# import random

# text = input("Введите текст для зашифровки : ")
# key = random.getrandbits(15)
# print("Ваш ключ для получения доступа к тексту : ", key)
# key_list = {key : text}

# def saveDict():
#     with open("hello.txt", "a") as fileW: #открывает существующий или создает новый файл
#         for key, value in key_list.items():
#            fileW.write(f"{key}::{value}\n")

#     fileW.close

# def openDict():
#     try:
#         with open("hello.txt", "r") as fileR:
#             try:
#                 list = fileR.readlines()
#                 listN = []

#                 for i in range(len(list)):
#                     list[i] = list[i][:len(list[i])-1]
#                     listN.append(list[i].split("::"))
#                     listN[i][0] = int(listN[i][0])
#             except Exception as e:
#                 print(e)
#             finally:
#                 fileR.close
#                 return dict(listN)
#     except Exception as ex:
#         print(ex)

# saveDict() #Сохранение новых данных в словарь в файл hello.txt

# key_list = openDict() #Чтение данных из hello.txt, возвращает данные
# #в виде словаря {key : text}
# print(key_list)