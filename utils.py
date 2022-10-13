from random import randint
from Classes.basic_word import BasicWord
import requests
import json


def load_random_word():
    '''
    - получит список слов с внешнего ресурса
    - выберет случайное слово
    - создаст экземпляр класса `BasicWord`
    :return: экземпляр
    '''

    path = requests.get('https://jsonkeeper.com/b/Q3BK')
    text_json = json.loads(path.text)
    random_number = randint(0, 2)

    word = text_json[random_number]["word"]
    subwords = text_json[random_number]["subword"]

    return BasicWord(word, subwords)



