from typing import NamedTuple, Self
from random import randint
from datetime import datetime


class Move(NamedTuple):
    x: int
    y: int


class BoardPosition(NamedTuple):
    x: int
    y: int

    def move(self, m: Move) -> Self:
        return type(self)(self.x + m.x, self.y + m.y)


POSSIBLE_MOVES = [
    Move(2, 1),
    Move(1, 2),
    Move(-1, 2),
    Move(-2, 1),
    Move(-2, -1),
    Move(-1, -2),
    Move(1, -2),
    Move(2, -1),
]


def reset_board(board: list[list[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 0


def is_valid_move(board: list[list[int]], position: BoardPosition) -> bool:
    if position.y < 0 or position.y >= len(board):
        return False
    if position.x < 0 or position.x >= len(board[0]):
        return False
    return board[position.y][position.x] == 0


def find_tour(board: list[list[int]]) -> tuple[bool, list[BoardPosition]]:
    current = BoardPosition(0, 0)
    board[0][0] = 1
    path = [current]
    num_squares = len(board) * len(board[0])

    while len(path) != num_squares:
        possible_move_pos = [i for i in range(8)]
        for _ in range(8):
            next_move_pos = randint(0, len(possible_move_pos) - 1)
            next_move = POSSIBLE_MOVES[possible_move_pos[next_move_pos]]
            possible_next_position = current.move(next_move)

            if is_valid_move(board, possible_next_position):
                current = possible_next_position
                path.append(current)
                board[current.y][current.x] = 1
                break

            possible_move_pos.remove(possible_move_pos[next_move_pos])

        else:
            return False, path
    return True, path


def main(length: int, width: int) -> None:
    board = [[0 for _ in range(width)] for _ in range(length)]
    tour_found = False

    print("Beginning to search for a valid tour. This might take up to 5 minutes.")
    print()

    start_time = datetime.now()
    num_attempts = 0
    while not tour_found:
        reset_board(board)
        num_attempts += 1
        tour_found, _ = find_tour(board)

    print(f"Valid tour found after {num_attempts} attempts.")
    print(f"Run took {(datetime.now() - start_time).seconds} seconds.")


if __name__ == "__main__":
    main(8, 8)
