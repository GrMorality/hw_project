def capitalize_string():
    """
    Функция возвращает изменённую строку,
    где первая буква каждого слова написана заглавными буквами.
    input_string — строка, которую нужно обработать
    """
    words = input().split()
    modified_words = [word.capitalize() for word in words]
    return ' '.join(modified_words)


print(capitalize_string())
