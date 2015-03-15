def board_to_string(board) :

    for row in board:
        print("|", " | ".join(row),"|")

    return

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

board_to_string(board)
