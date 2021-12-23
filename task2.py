# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

word_list = ['class', 'function', 'method']
b_word_list = [b'class', b'function', b'method']
for b_word in b_word_list:
    print(f'{b_word} - тип {type(b_word)}, длина {len(b_word)}')
