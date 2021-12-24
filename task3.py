# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

word_list = ['attribute', 'класс', 'функция', 'type']
#  b'класс', b'функция' пичарм сразу подсвечивает и пишет по русски: bytes can only contain ASCII literal characters
b_word_list = [b'attribute', b'класс', b'функция', b'type']
for b_word in b_word_list:
    print(f'{b_word} - тип {type(b_word)}, длина {len(b_word)}')