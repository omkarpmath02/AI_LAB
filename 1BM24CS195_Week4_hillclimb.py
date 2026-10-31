

import random

def heuristic(board, n):
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def display_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def hill_climbing(n):

    # Initial random state
    board = [random.randint(0, n-1) for _ in range(n)]

    iteration = 1

    while True:

        current_h = heuristic(board, n)

        print("\n========== ITERATION", iteration, "==========")
        print("Current State:")
        display_board(board, n)
        print("Heuristic =", current_h)

        # Goal test
        if current_h == 0:
            print("\nGOAL STATE REACHED!")
            return board

        best_board = board[:]
        best_h = current_h

        # Find best neighbor
        for col in range(n):
            for row in range(n):

                if board[col] != row:

                    neighbor = board[:]
                    neighbor[col] = row

                    h = heuristic(neighbor, n)

                    if h < best_h:
                        best_h = h
                        best_board = neighbor[:]

        # Local minimum check
        if best_h >= current_h:
            print("\nNo better neighbor found!")
            print("Local minimum reached.")
            return None

        # Display only selected next state
        print("\nSelected Next State:")
        display_board(best_board, n)
        print("Heuristic =", best_h)

        board = best_board
        iteration += 1


# Main program
n = int(input("Enter number of queens: "))

solution = hill_climbing(n)

if solution is not None:
    print("\n========== FINAL SOLUTION ==========")
    display_board(solution, n)
    print("Heuristic =", heuristic(solution, n))
else:
    print("\nSolution not found. Try running again.")
