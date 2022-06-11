def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts=[0]*rows
    for row in range(rows):
        lst_of_lsts[row]=list(map(int,input().split()))
    return rows ,len(lst_of_lsts[0]),lst_of_lsts

if __name__ == '__main__':
    rows,cols,matrix=read_matrix()
    elem=int(input())
    for idx,rows in enumerate(matrix):
        if elem in rows:
            print(f"found in col {idx}" )
            break


  
    
        

        

