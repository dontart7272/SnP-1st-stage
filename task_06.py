'''
Разработать методы для программы Камень-Ножницы-Бумага. При реализации
обработки исключений важно не использовать встроенные классы ошибок с
передачей им сообщения, а разработать классы с представленными ниже
названиями.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень, и
функционировать следующим образом:

• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.
'''

class WrongNumberOfPlayersError(ValueError):
    '''Класс исключения, вызывается при несоответствии количества игроков (2))'''

    def __init__(self, players: int = 0) -> None:
        super().__init__(players)
        self.players: int = players

    def __str__(self) -> str:
        return f"Число игроков отлично от 2 (Передано: {self.players})" \
               if self.players \
               else "Число игроков отлично от 2"



class NoSuchStrategyError(ValueError):
    '''Класс исключения, вызывается при использовании несуществующего хода'''

    def __init__(self, player: str = '', move: str = '') -> None:
        self.player: str = player
        self.move: str = move

    def __str__(self) -> str:
        return f"Передан несуществующий ход для игрока (Возможные ходы: P, S, R; Передано: {self.move})" \
                if self.player and self.move \
                else "Число игроков отлично от 2 (Возможные ходы: P, S, R)"



# Словарь соответствия хода числовому значению
MOVE_INDEX = {
    'R': 0,
    'P': 1,
    'S': 2
}


def rps_game_winner(moves: list[list[str]]) -> str:
    '''
    Функция для определения победеителя в игре Камень, Ножницы, Бумага.

    Логика:
    Каждому из возможных ходов присваивается числовое значение
    Камень - 0
    Бумага - 1
    ножницы - 2

    При проверке победителя вычитаем из числа, которое соответствует ходу игрока 2 число,
    которое соответствует ходу игрока 1. Вычисляем остаток от деления на 3 из полученной разности.

    В итоге получем число, которое соответствует номеру победившего игрока
    либо 0 - тоже соответствует первому игроку.
    '''

    # Проверяю, что игроков не более двух
    if len(moves) > 2:
        raise WrongNumberOfPlayersError(len(moves))

    # Проверяю, что каждый игрок выбрал существующий вариант хода
    lst = [move in 'PRS' for player, move in moves]

    if not all(lst):
        raise NoSuchStrategyError(*moves[lst.index(False)])

    # Основная логика проверки, которая описана в шапке
    winner = (MOVE_INDEX[moves[0][1]] - MOVE_INDEX[moves[1][1]]) % 3

    return f'{moves[0][0]} {moves[0][1]}' if winner in (0, 1) \
        else f'{moves[1][0]} {moves[1][1]}'




if __name__ == '__main__':
    try:
        rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
    except WrongNumberOfPlayersError:
        print('Тест 1 пройден')
    try:
        rps_game_winner([['player1', 'P'], ['player2', 'A']])
    except NoSuchStrategyError:
        print('Тест 2 пройден')

    assert rps_game_winner([['player1', 'P'], ['player2', 'S']]) == 'player2 S'; print('Тест 3 пройден')
    assert rps_game_winner([['player1', 'P'], ['player2', 'P']]) == 'player1 P'; print('Тест 4 пройден')
    print('Все тесты пройдены успешно')
