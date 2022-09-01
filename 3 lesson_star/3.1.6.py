letter = input("Введите букву\n")

_alphabet_ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u", "y"]

vowels_big = ["A", "E", "I", "O", "U", "Y"]

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p",
              "q", 'r', "s", "t", "v", "w", "x", "z"]

consonants_big = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P",
              "Q", "R", "S", "T", "V", "W", "X", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

punctuation_mark = ["!", ",", ".", "/", ";", ":"]

if letter in vowels:
    print("Это маленькая гласная буква")

elif letter in vowels_big:
    print("Это большая гласная буква")

elif letter in consonants:
    print("Это маленькая согласная буква")

elif letter in consonants_big:
    print("Это большая согласная буква")

elif letter in numbers:
    print("Это цифра")

elif letter in punctuation_mark:
    print("Это знак препинания")

else:
    print("Это непонятно что")
