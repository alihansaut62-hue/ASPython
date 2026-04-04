start_mod = ['здарова', 'списк', 'я вспомнил что на рус можно писать ', 'пока что так']
end_mod = []
while start_mod:
    cor_mod = start_mod.pop()
    print(f"отправляется от Я {cor_mod}")
    end_mod.append(cor_mod)

print("\nпринитые сообщения:")
for cor_mod in end_mod:
    print(cor_mod)