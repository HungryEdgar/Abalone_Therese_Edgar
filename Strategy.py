
def black_strategy(board,state):
    my_pos = []
    adv_pos = []
    line = 0
    col = 0
    for line in range(len(board)):
        for col in range(len(board[0])):
            if board[line][col] == "B":
                my_pos.append([line, col])
            if board[line][col] == "W":
                adv_pos.append([line, col])
            col += 1
        line += 1
    print(my_pos)


def white_strategy(board,state):
    my_pos = []
    adv_pos = []
    line = 0
    col = 0
    for line in range(len(board)):
        for col in range(len(board[0])):
            if board[line][col] == "W":
                my_pos.append([line, col])
            if board[line][col] == "B":
                adv_pos.append([line, col])
            col += 1
        line += 1
    print(my_pos)
    if state["board"][3][3] == 'E':
        move = {
            "marbles": [[0, 0], [1, 1], [2, 2]],
            "direction": "SE"
        }

    if state["board"][3][4] == 'E':
        move = {
            "marbles": [[0, 1], [1, 2], [2, 3]],
            "direction": "SE"
        }

    if state["board"][3][5] == 'E':
        move = {
            "marbles": [[0, 2], [1, 3], [2, 4]],
            "direction": "SE"
        }
    # on répète cette opération
    if state["board"][4][4] == 'E' and state["board"][3][3] == 'W':
        move = {
            "marbles": [[1, 1], [2, 2], [3, 3]],
            "direction": "SE"
        }

    if state["board"][4][5] == 'E' and state["board"][3][4] == 'W':
        move = {
            "marbles": [[1, 2], [2, 3], [3, 4]],
            "direction": "SE"
        }

    if state["board"][4][6] == 'E' and state["board"][3][5] == 'W':
        move = {
            "marbles": [[1, 3], [2, 4], [2, 5]],
            "direction": "SE"
        }

    # là on est déjà au 10eme tour
    if state["board"][4][4] == 'W' and state["board"][3][3] == 'W' and state["board"][2][2] == 'W' and \
            state["board"][5][5] == 'B' and state["board"][6][6] == 'E':
        move = {
            "marbles": [[2, 2], [3, 3], [4, 4]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 5]],  # pions noirs
            "direction": "SE"
        }

    if state["board"][4][4] == 'W' and state["board"][3][3] == 'W' and state["board"][2][2] == 'W' and \
            state["board"][5][5] == 'B' and state["board"][6][6] == 'B':
        move = {
            "marbles": [[2, 2], [3, 3], [4, 4]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 5], [6, 6]],  # pions noirs
            "direction": "SE"
        }
    if state["board"][2][3] == 'W' and state["board"][3][4] == 'W' and state["board"][4][5] == 'W' and \
            state["board"][5][6] == 'B' and state["board"][6][7] == 'E':
        move = {
            "marbles": [[2, 3], [3, 4], [4, 5]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 6]],  # pions noirs
            "direction": "SE"
        }
    if state["board"][2][3] == 'W' and state["board"][3][4] == 'W' and state["board"][4][5] == 'W' and \
            state["board"][5][6] == 'B' and state["board"][6][7] == 'B':
        move = {
            "marbles": [[2, 3], [3, 4], [4, 5]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 6], [6, 7]],  # pions noirs
            "direction": "SE"
        }
    if state["board"][2][4] == 'W' and state["board"][3][5] == 'W' and state["board"][4][6] == 'W' and \
            state["board"][5][7] == 'B' and state["board"][6][8] == 'E':
        move = {
            "marbles": [[2, 4], [3, 5], [4, 6]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 7]],  # pions noirs
            "direction": "SE"
        }
    if state["board"][2][4] == 'W' and state["board"][3][5] == 'W' and state["board"][4][6] == 'W' and \
            state["board"][5][7] == 'B' and state["board"][6][8] == 'B':
        move = {
            "marbles": [[2, 4], [3, 5], [4, 6]],  # pions blancs
            "direction": "SE"
        }
        move = {
            "marbles": [[5, 7][6, 8]],  # pions noirs
            "direction": "SE"
        }
