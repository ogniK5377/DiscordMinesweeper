import random, sys
GAMEBOARD = []

BOARD_X = 9
BOARD_Y = 9
MINECOUNT = 25
SPOILERS_CHAR = '||'
CHARACTER_LOOKUP = {
    '0': 'black_square_button',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'B': 'bomb',
    'X': 'warning'
}

def generate_board():
    global GAMEBOARD
    for i in range(0, BOARD_X):
        GAMEBOARD.append([])
        for _ in range(0, BOARD_Y):
            GAMEBOARD[i].append(0)

def is_bomb(x, y):
    return GAMEBOARD[x][y] == 'B'

def check_block(x, y):
    if x < 0:
        return 'X'
    if x > BOARD_X-1:
        return 'X'
    if y < 0:
        return 'X'
    if y > BOARD_Y-1:
        return 'X'
    return GAMEBOARD[x][y]

def count_bombs(x, y):
    bomb_count = 0
    if check_block(x-1, y) == 'B':
        bomb_count += 1
    if check_block(x-1, y+1) == 'B':
        bomb_count += 1
    if check_block(x, y+1) == 'B':
        bomb_count += 1
    if check_block(x+1, y+1) == 'B':
        bomb_count += 1
    if check_block(x+1, y) == 'B':
        bomb_count += 1
    if check_block(x+1, y-1) == 'B':
        bomb_count += 1
    if check_block(x, y-1) == 'B':
        bomb_count += 1
    if check_block(x-1, y-1) == 'B':
        bomb_count += 1
    return bomb_count

def get_number_format(num):
    if num < 10 and num >= 0:
        return CHARACTER_LOOKUP[str(num)]
    return CHARACTER_LOOKUP['X']

def random_vector(x_max, y_max):
    return random.randint(0, x_max), random.randint(0, y_max)

def generate_bombs():
    global GAMEBOARD
    mine_count = 0
    while mine_count < MINECOUNT:
        x, y = random_vector(BOARD_X - 1, BOARD_Y - 1)
        if is_bomb(x, y):
            continue
        GAMEBOARD[x][y] = 'B'
        mine_count += 1

def generate_numbers():
    global GAMEBOARD
    for x in range(0, BOARD_X):
        for y in range(0, BOARD_Y):
            if is_bomb(x, y):
                continue
            GAMEBOARD[x][y] = str(count_bombs(x, y))

def place_within_tag(element):
    return SPOILERS_CHAR + element + SPOILERS_CHAR

def generate_emoji_board():
    board = ''
    for x in range(0, BOARD_X):
        tmp = ''
        for y in range(0, BOARD_Y):
            if check_block(x, y) == '0':
                tmp += ':' + CHARACTER_LOOKUP[GAMEBOARD[x][y]] + ':'
                continue
            else:
                if len(tmp) > 0:
                    board += place_within_tag(tmp)
                    tmp = ''
            board += place_within_tag(':' + CHARACTER_LOOKUP[GAMEBOARD[x][y]] + ':')
        if len(tmp) > 0:
            board += place_within_tag(tmp)
            tmp = ''
        board += '\n'

    print(board)

def main(argc, argv):
    global BOARD_X
    global BOARD_Y
    global MINECOUNT

    try:
        if argc < 4:
            print('%s <x size> <y size> <mine count>' % argv[0])
            return 1
        BOARD_X = int(argv[1])
        BOARD_Y = int(argv[2])
        MINECOUNT = int(argv[3])
        generate_board()
        generate_bombs()
        generate_numbers()
        generate_emoji_board()
    except Exception as ex:
        print('An error has occured, %s' % ex)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
