class Player:
    '''
    Содержит информацию об игроке
    '''
    words_used = []


    def __init__(self, user_name):
        self.user_name = user_name


    def get_count_the_words_used(self):
        '''
        получение количества использованных слов
        :return: int(element)
        '''
        return len(self.words_used)


    def add_to_the_used_words(self, word):
        '''
        добавление слова в использованные слова - список
        :return: None
        '''
        self.words_used.append(word)

    def check_words_isnew(self, word):
        '''
        проверка использования данного слова до этого
        :return: bool
        '''
        if word not in self.words_used:
            return True
        return False

    # Получение всех используемых слов?

    def __repr__(self):
        return f"Player({self.words_used},{self.user_name})" \
