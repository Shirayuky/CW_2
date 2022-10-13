from Classes.basic_word import BasicWord
from Classes.player import Player
from utils import load_random_word
import requests
import sys


#Welcome
name = input("Приветствую тебя, Игрок!\nНазови свои имя: ")
# user_welcome = input(f"{name.title()}, ты готов начать?\nДа/нет: ")
# if user_welcome.lower() == "нет":
#     print("Ок, тогда в другой раз ;)")
#     sys.exit()
# print("Отлично! Вот твое задание:")

player = Player(user_name=name)

# original_word - возвращает объект класса BasicWord
original_word = load_random_word()
subwords_count = original_word.count_the_numb_of_subswords()

print(f"Составьте {subwords_count} из слова {original_word.upper()}")
print("ВНИМАНИЕ: слова должны быть не короче 3-х букв!")
print("И так, ваше первое слово...\n")

# Пока пользователь угадал меньше слов, чем есть в базе
while player.get_count_the_words_used() < subwords_count:
    word = input().lower()

    if word == "stop" or "стоп":
        break

    if len(word) < 3:
        print("Это слово слишком короткое! Попробуйте снова :)")
        # И переходим к след слову
        continue

    if original_word.check_words(word) and player.check_words_isnew():
        player.add_to_the_used_words(word)
        print("Супер, такое слово есть!")
    else:
        print("Упс...Не то\n1. Либо такого слова нет\n2. Либо вы написали слово повторно\nПопробуйте снова :)")

print(f"Игра окончена!\nВы угадали {player.get_count_the_words_used()} слов(а)!")