def is_palindrome(word):
    """
    Проверка является ли слово палиндромом
    """
    word_without_space = word.replace(" ", "")
    word_low = word_without_space.lower()
    reversed_word = word_low[::-1]
    if word_low == reversed_word:
        return True
    else:
        return False

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")
