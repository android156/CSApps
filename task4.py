# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

word_list = ['разработка', 'администрирование', 'protocol', 'standard']
byte_word_list = []
print('Преобразование строка -> байты')
for word in word_list:
    byte_word = word.encode("utf-8")
    byte_word_list.append(byte_word)
    print(f'{word} - тип {type(word)}')
    print(f'{word} - в Юникоде {byte_word} - тип {type(word.encode("utf-8"))}')

print('Преобразование байты -> строка')
for byte_word in byte_word_list:
    word = byte_word.decode("utf-8")
    print(f'Байты {byte_word} -> {word}')