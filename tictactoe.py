tic=[
    ['[]','[]','[]'],
    ['[]','[]','[]'],
    ['[]','[]','[]']
]
def display():
    for i in tic:
        print('')
        for j in i:
            print(j,end=' ')

def player1(tic,row,col):
    tic[row][col]='[X]'
def player2(tic,row,col):
    tic[row][col]='[O]'
def wincond(tic,sym='0'):
    if tic[0][0]==tic[0][1]==tic[0][2] and tic[0][0]in sym:
        return True
    elif tic[1][0]==tic[1][1]==tic[1][2] and tic[1][0] in sym :
        return  True
    elif tic[2][0]==tic[2][1]==tic[2][2] and tic[2][0] in sym:
        return True
    elif tic[0][0]==tic[1][1]==tic[2][2] and tic[0][0] in sym:
        return True
    elif tic[2][0]==tic[1][1]==tic[0][2] and tic[2][0] in sym:
        return True
    elif tic[0][0]==tic[1][0]==tic[2][0] and tic[0][0]  in sym:
        return True
    elif tic[0][1]==tic[1][1]==tic[1][2] and tic[0][1] in sym :
        return True
    elif tic[0][2]==tic[1][2]==tic[2][2] and tic[0][2] in sym:
        return True
    else:
        return  False


print('Player 1= X')
print('Player 2= O')
st=wincond(tic)
while st==False:
    row=int(input('\n Enter the row'))
    col=int(input('Enter the col'))
    player1(tic,row,col)
    display()
    sym='[X]'
    w1=wincond(tic,sym)
    if w1==True:
        print("\n Player 1 Wins")
        break
    else:
        row=int(input('\nEnter the row'))
        col=int(input('Enter the col'))
        player2(tic,row,col)
        display()
        sym='[O]'
        w2=wincond(tic,sym)
        if w2==True:
            print("\n Player 2 Wins")
            st=True
        else:
            st=False


