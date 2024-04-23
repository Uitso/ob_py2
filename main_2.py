lst_in = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [5, 4, 3]]

a = [[x[i] for x in lst_in] for i in range(len(lst_in[0]))]

for row in a:
    print(*row)
