import json


class BasicWord:
    '''
    Содержит все данные необходимые для работы
    '''
    # original_word = None
    # set_of_acceptable_subswords = None



    def __init__(self, original_word, set_of_acceptable_subswords):
        self.set_of_acceptable_subswords = set_of_acceptable_subswords
        self.original_word = original_word


    def check_words(self, user_word):
        '''
        проверку введенного слова в списке допустимых подслов
        :return: bool
        '''
        if user_word in self.set_of_acceptable_subswords:
            return True
        return False

    def count_the_numb_of_subswords(self):
        '''
        подсчет количества подслов
        :return: int(element)
        '''
        return len(self.set_of_acceptable_subswords)


    def __repr__(self):
        return f"BasicWord({self.set_of_acceptable_subswords}, {self.original_word})"
