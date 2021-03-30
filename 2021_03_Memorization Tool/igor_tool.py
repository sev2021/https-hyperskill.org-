import db_worker as dw


class Game:

    def __init__(self):
        self.main_menu = {
            '1': ('Add flashcards', self.input_card),
            '2': ('Practice flashcards', self.practice),
            '3': ('Exit', self.exit),
        }
        self.cards = dw.results
        self.boxes = 3
        self.cards_score = {}
        self.menu(self.main_menu, key_format='n')

    @staticmethod
    def menu(menu_items, key_format=None, **kwargs):
        def not_an_option(**kws):
            print(f'{kws["command"]} is not an option\n')

        def print_menu(menu):
            format_dict = {'s': lambda s: f'press "{s}" ', 'n': lambda n: f'{n}. ', None: lambda s: s}
            for key, value in menu.items():
                key = format_dict.get(key_format, format_dict[None])(key)
                print(f'{key}{value[0]}')
        try:
            while True:
                print_menu(menu_items)
                kwargs['command'] = input()
                print()
                menu_items.get(kwargs['command'], (None, not_an_option))[1](**kwargs)
        except StopIteration:
            pass

    def input_card(self, **kwargs):  # number 1 on main menu
        def input_true(text):
            while True:
                result = input(f'{text}:\n')
                if not result:
                    continue
                return result

        def add_card(**kws):
            dw.add_cards(input_true('Question'), input_true('Answer'))
            print()
        input_card_menu = {
            '1': ('Add a new flashcard', add_card),
            '2': ('Exit', self.exit),
        }
        self.menu(input_card_menu, key_format='n')

    def practice(self, **kwargs):  # number 2 on main menu
        def check_learning(**kws):
            self.menu(learning_menu, key_format='s', **kws)
            self.exit()

        def show_answer(**kws):
            if kws['command'] == 'y':
                print(f'Answer: {kws["card"].answer}')
            check_learning(**kws)
            self.exit()

        def true_answer(**kws):
            self.cards_score[kws['card']] += 1
            if self.cards_score[kws['card']] == 3:
                self.delete_card(**kws)
            self.exit()

        def false_answer(**kws):
            self.cards_score[kws['card']] = 0
            self.exit()

        practice_menu = {
            'y': ('to see the answer:', show_answer),
            'n': ('to skip:', show_answer),
            'u': ('to update:', self.update_card),
        }
        learning_menu = {
            'y': ('if your answer is correct:', true_answer),
            'n': ('if your answer is wrong:', false_answer),
        }

        if self.cards():
            for card in self.cards():
                self.cards_score[card] = self.cards_score.get(card, 0)
                print(f'Question: {card.question}')
                self.menu(practice_menu, key_format='s', card=card, **kwargs)
        else:
            print('There is no flashcard to practice!\n')

    @staticmethod  # number 3 on main menu
    def exit(**kwargs):
        raise StopIteration

    @staticmethod
    def delete_card(**kwargs):
        dw.delete_card(kwargs['card'].id)
        Game.exit()

    def update_card(self, **kwargs):
        def edit_card(card, **kws):
            def input_format(word, val):
                return f'current {word}: {val}\nplease write a new {word}:\n'
            dw.edit_card(card.id,
                         input(input_format('question', card.question)),
                         input(input_format('answer', card.answer))
                         )
            self.exit()

        update_menu = {
            'd': ('to delete the flashcard:', self.delete_card),
            'e': ('to edit the flashcard:', edit_card),
        }
        self.menu(update_menu, key_format='s', **kwargs)
        self.exit()


if __name__ == '__main__':
    Game()
    print('Bye!')
