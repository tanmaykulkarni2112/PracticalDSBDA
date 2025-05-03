def solve_n_queens(n):
    cols = set()
    posd = set()  # r + c
    negd = set()  # r - c

    board = [["."] * n for _ in range(n)]
    res = []

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in posd or (r - c) in negd:
                continue

            cols.add(c)
            posd.add(r + c)
            negd.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            cols.remove(c)
            posd.remove(r + c)
            negd.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


n = 4
solutions = solve_n_queens(n)
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in solution:
        print(row)
    print()
