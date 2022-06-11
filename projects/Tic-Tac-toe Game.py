def print_board(tiles):
    [print(row) for row in board ]
def validation(r,c,tiles_num):
    return not 0<= r < tiles_num or not 0 <=c<tiles_num or board[r][c] !="_"
def is_winner(board,tiles_num):
    winner=None
    for i in range(tiles_num):

        if board[i][0]==board[i][1]==board[i][2] !="_": #HORIZONTAL 
            winner=board[i][0]
            break
        if board[0][i]==board[1][i]==board[2][i] !="_": #vertical 
            winner=board[0][i] 
            break
    if board[1][1]=="_":
        if board[0][0]==board[1][1]==board[2][2]:
            winner=board[1][1]

    return f"{winner} is the winner"
    return True


if __name__ == '__main__':

    tiles_num=int(input("enter grid size:"))
    tied,turn=0,0 #to make it easy to track which symbol to put 


    board=[['_']* tiles_num for rows in range(tiles_num) ]

    sympols='XO'
    while True:
        if tied== tiles_num*tiles_num:
            print("Tie!")
            break
        print_board(tiles_num)
        r,c=list(map(int,input(f"Player {sympols[turn]},make a move:").split())) #we take input as zero pos but the user dont know and enter the normal position
        r,c=r-1,c-1
        if   validation(r,c,tiles_num):
            print("Invalid location.Try again")
            continue
        else:
            board[r][c] = sympols[turn]
            winner=None
        for i in range(tiles_num):

            if board[i][0]==board[i][1]==board[i][2] !="_": #HORIZONTAL 
                winner=board[i][0]
                break
            if board[0][i]==board[1][i]==board[2][i] !="_": #vertical 
                winner=board[0][i] 
                break
        print(f"{winner} is the winner")
     

        turn =1-turn #here to change the symbol from X to O

######didnt finish the diagonal check 



        





