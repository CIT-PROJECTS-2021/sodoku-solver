from sodokusolver.sodoku import Sodoku


def main():
    # create a sodoku puzzle
    sodoku = Sodoku()
    # print the sodoku puzzle
    print("Sodoku puzzle:")
    sodoku._print_sodoku()
    # solve the sodoku puzzle
    sodoku._solve_sodoku()
    # print the sodoku puzzle solution
    print("Sodoku puzzle solution:")
    sodoku._print_sodoku_solution()
    # print the number of sodoku puzzle solutions
    sodoku._print_sodoku_solution_count()
    # print the time taken to solve the sodoku puzzle
    sodoku._print_sodoku_solution_time()


if __name__ == "__main__":
    main()