def is_palindrome(word):
    processed_word = ''.join(filter(str.isalnum, word)).lower()
    return processed_word == processed_word[::-1]


user_input = input('Введите слово: ')
if is_palindrome(user_input):
    print(f'"{user_input}" - палиндром')
else:
    print(f'"{user_input}" - не палиндром')
