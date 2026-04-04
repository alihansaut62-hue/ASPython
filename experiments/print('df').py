import nltk
import random

while True:
    def get_rank(text1, text2):
        distance = nltk.edit_distance(text1, text2)
        average_length = (len(text1) + len(text2)) / 2
        return distance / average_length

    qw = input("Задай мне вопрос: ")
    if qw == 'q':
        break


    data_base = [
        {
            "qw": "как дела",
            "answer": ["дела отлично", "все супер", "не жалуюсь"],
        },
        {
            "qw": "что ты умеешь",
            "answer": ["я могу разговаривать с тобой", "я могу учиться", "я могу помогать тебе"],
        },
        {
            "qw": "где ты живешь",
            "answer": ["я живу в облаке", "я живу в интернете", "я живу на сервере"],
        },
        {
            "qw": "который час",
            "answer": ["у меня нет часов", "я не слежу за временем", "время - это иллюзия"],
        }
    ]

    for pair in data_base:
        if get_rank(qw, pair["qw"]) < 0.5:
            print(random.choice(pair["answer"]))
            break
    else:
        print("Я не понимаю вопрос 😔")
