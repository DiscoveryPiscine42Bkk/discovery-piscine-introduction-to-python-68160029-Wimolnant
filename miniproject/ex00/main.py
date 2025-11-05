import sys
from checkmate import check_mate 

def main():
    board_rows = sys.argv[1:]
    
    if not board_rows:
        board = [
            "..R..",
            ".....",
            "..K..",
            ".....",
            "....."
        ]
        check_mate(board)
        return

    check_mate(board_rows)


if __name__ == "__main__":
    main()