def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts=[0]*rows
    for row in range(rows):
        lst_of_lsts[row]=list(map(int,input().split()))
    return rows ,len(lst_of_lsts[0]),lst_of_lsts

if __name__ == '__main__':
    rows,cols,matrix=read_matrix()
    max_val=None
    max_row=None
    max_cols= None
    for row_idx,row in enumerate(matrix) :
        for cols_idx,value in enumerate(row):
            if max_val is None or max_val <= value:
                max_val=value
                max_row=row_idx
                max_cols=cols_idx

                
    
    print(f"max value at position({max_row},{max_cols}) with value ={max_val}")
        

        

