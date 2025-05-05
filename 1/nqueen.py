def nqueen(n):
    cols = set()
    positive = set()
    negative = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if n == r:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return 

        for c in range(n):

            if c in cols or (r+c) in positive or (r - c) in negative:
                continue

            cols.add(c)
            positive.add(c + r)
            negative.add( r - c)
            board[r][c] = "Q"

            backtrack(r+1)

            cols.remove(c)
            positive.remove(r + c)
            negative.remove(r - c)
            board[r][c] = "."
    
    backtrack(0)
    return res

soln = nqueen(4)
for i,s in enumerate(soln):
    print(i +1)
    for rows in s:
        print(rows)
    print()