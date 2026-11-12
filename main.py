from random import shuffle

win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]

def start():
    field = ['_']*9
    print("\nДобро пожаловать в игру 'Крестики-нолики'!")
    f_player = read_name("Введите имя 1-го игрока: ")
    s_player = read_name("Введите имя 2-го игрока: ")
    while f_player.lower() == s_player.lower():
        print("Имена должны отличаться!")
        s_player = read_name("Введите имя 2-го игрока: ")
    players = [f_player, s_player]
    shuffle(players)
    print(f"\n{players[0].title()} - крестики!")
    print(f"{players[1].title()} - нолики!\n")
    symbols = ['X', 'O']
    for turn in range(9):
        if turn % 2 == 0:
            name, symbol = players[0], symbols[0]
        else:
            name, symbol = players[1], symbols[1]
        print(f"{name.title()}, Ваш ход!\n")
        make_move(field, symbol)

        if win(field, symbol):
            print(f"Победил {name.title()}!")
            return

    print("Ничья!") 

def read_number(prompt):
    while True:
        value = input(prompt).strip()
        if value in ('1', '2', '3'):
            return int(value)
        print("Введите число от 1 до 3!")

def read_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Имя не может быть пустым!")

def make_move(field, symbol):
    while True:
        line =  read_number('Введите номер строки(1-3): ')
        column =  read_number('Введите номер столбца(1-3): ')

        index = (line-1)*3 + (column-1)

        if field[index] != '_':
            print("\nЭта клетка уже занята!\n")
            continue

        field[index] = symbol

        print('\nИгровое поле:')
        print('', *field[:3], '\n', *field[3:6], '\n', *field[6:], '\n')

        return

def win(field, symbol):
    for a, b, c in win_comb:
        if field[a] == field[b] == field[c] == symbol:
            return True
    return False

def main():

if __name__ == '__main__':
    main()
