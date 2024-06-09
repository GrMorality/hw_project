def capitalize_string():
    words = input().split()
    modified_words = [word.capitalize() for word in words]
    return ' '.join(modified_words)


print(capitalize_string())
