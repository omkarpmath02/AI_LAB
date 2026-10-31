
import random
import math

def heuristic(board, n):
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
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


def simulated_annealing(n):

    if n == 2 or n == 3:
        print("No solution exists for N =", n)
        return None

    max_restarts = 50

    for restart in range(max_restarts):

        board = [random.randint(0, n-1) for _ in range(n)]

        temperature = 100
        cooling_rate = 0.995
        iteration = 1

        print("\n========== NEW START ==========")
        print("Initial State:")
        display_board(board, n)
        print("Heuristic =", heuristic(board, n))

        while temperature > 0.01:

            current_h = heuristic(board, n)

            if current_h == 0:
                print("\nGOAL STATE REACHED!")
                return board

            # Generate random neighbor
            neighbor = board[:]

            col = random.randint(0, n-1)
            row = random.randint(0, n-1)

            while row == board[col]:
                row = random.randint(0, n-1)

            neighbor[col] = row

            new_h = heuristic(neighbor, n)

            delta = current_h - new_h

            # Acceptance condition
            if delta > 0:
                accept = True
            else:
                probability = math.exp(delta / temperature)
                accept = random.random() < probability

            print("\nIteration:", iteration)
            print("Temperature:", round(temperature, 2))

            if accept:
                board = neighbor

                print("Selected Next State:")
                display_board(board, n)
                print("Heuristic =", new_h)
            else:
                print("Next state rejected.")
                print("Current State:")
                display_board(board, n)
                print("Heuristic =", current_h)

            temperature *= cooling_rate
            iteration += 1

        if heuristic(board, n) == 0:
            print("\nGOAL STATE REACHED!")
            return board

    print("\nSolution not found after maximum restarts.")
    return None


# Main program
n = int(input("Enter number of queens: "))

if n < 1:
    print("Enter a positive number.")
else:
    solution = simulated_annealing(n)

    if solution is not None:
        print("\n========== FINAL SOLUTION ==========")
        display_board(solution, n)
        print("Final Heuristic =", heuristic(solution, n))
