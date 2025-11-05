def check_mate(board_rows):
    
    board = board_rows
    size = len(board)
    king_r, king_c = -1, -1

    for r in range(size):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                king_r, king_c = r, c
                break
        if king_r != -1:
            break

    if king_r == -1:
        print("Fail") 
        return

    pawn_attack_positions = [
        (king_r - 1, king_c - 1),  
        (king_r - 1, king_c + 1),  
        (king_r + 1, king_c - 1),  
        (king_r + 1, king_c + 1)   
    ] 

    for r, c in pawn_attack_positions:
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'P':
            print("Success")
            return

    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    for dr, dc in straight_dirs:
        r, c = king_r + dr, king_c + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            elif piece != '.': 
                break
            r, c = r + dr, c + dc

    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

    for dr, dc in diag_dirs:
        r, c = king_r + dr, king_c + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            elif piece != '.': 
                break
            r, c = r + dr, c + dc

    print("Fail")