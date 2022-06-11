def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts=[0]*rows
    for row in range(rows):
        lst_of_lsts[row]=list(map(int,input().split()))
    return rows ,len(lst_of_lsts[0]),lst_of_lsts

if __name__ == '__main__':
    rows,cols,matrix=read_matrix()
                                     ###sum of last row
    last_rows_sums=sum(matrix[-1])
    last_cols_sums= sum([rows[-1] for rows in matrix])

    left_diago= sum([rows[idx]for idx,rows in enumerate(matrix)])
    right_diago= sum([rows[-(idx+1)]for idx,rows in enumerate(matrix)])

    print(last_rows_sums,last_cols_sums)
    print(left_diago,right_diago)

        



    

        

