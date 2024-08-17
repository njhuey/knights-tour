#include <iostream>
using namespace std;

void clear_board(int **board) {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      board[i][j] = 0;
    }
  }
}

int main(int argc, char *argv[]) {
  cout << "Starting the search for a valid knight's tour." << endl;

  int board[8][8];
  clear_board(board);

  return 0;
}
