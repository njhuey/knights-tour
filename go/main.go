package main

import (
	"fmt"
	"math/rand"
	"time"
)

var MOVES = [8][2]int8{
	{2, 1},
	{1, 2},
	{-2, 1},
	{-1, 2},
	{2, -1},
	{1, -2},
	{-2, -1},
	{-1, -2},
}

func printBoard(board [][]byte) {
	for i := 0; i < len(board); i++ {
		fmt.Println(board[i])
	}
}

func resetBoard(board [][]byte) {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = 0
		}
	}
}

func isValidMove(board [][]byte, i, j int) bool {
	return i >= 0 && j >= 0 && i < len(board) && j < len(board) && board[i][j] != 1
}

func runSimulation(board [][]byte) bool {
	curr_i, curr_j := 0, 0
	board[curr_i][curr_j] = 1
	n := len(board) * len(board[0])
	for i := 1; i < n; i++ {
		order := []int{0, 1, 2, 3, 4, 5, 6, 7}
		rand.Shuffle(len(order), func(i, j int) {
			order[i], order[j] = order[j], order[i]
		})

		flag := false
		for _, move_num := range order {
			new_i := curr_i + int(MOVES[move_num][0])
			new_j := curr_j + int(MOVES[move_num][1])
			if isValidMove(board, new_i, new_j) {
				curr_i, curr_j = new_i, new_j
				flag = true
				board[curr_i][curr_j] = 1
				break
			}
		}
		if !flag {
			return false
		}

	}

	return true
}

func knightsTour(board_size int) {
	board := make([][]byte, board_size)
	for i := 0; i < board_size; i++ {
		board[i] = make([]byte, board_size)
	}

	attempts := 0
	flag := false
	start_time := time.Now()
	for !flag {
		attempts++
		flag = runSimulation(board)
		resetBoard(board)
	}
	time_elapsed := time.Since(start_time)
	fmt.Println("Num attempts: ", attempts)
	fmt.Println("Time elapsed: ", time_elapsed)
}

func main() {
	knightsTour(8)
}
