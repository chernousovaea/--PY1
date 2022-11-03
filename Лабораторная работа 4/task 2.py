def get_count_char(str_):
    str_ = str_.lower()

    dict_letters = {}

    for i in str_:
        if i.isalpha():
            if i in dict_letters:
                dict_letters[i] += 1
            else:
                dict_letters[i] = 1

    return dict_letters

def get_dict_symbol(dict):
    dict_percentage_letters = {}
    count = 0

    for i in dict:
       count += dict[i]

    for i in dict:
        dict_percentage_letters[i] = round((dict[i] / count * 100), 1)

    return dict_percentage_letters

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
