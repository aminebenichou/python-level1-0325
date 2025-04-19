cells=[1,2,3,4,5,6,7,8,9]

def find_winner(condition_num, x, counter):
    j=0
    while j<condition_num:
        if cells[j] == cells[j+x] == cells[j+(2*x)]:
            print("You Win")
            return True
        j += counter
    return False

def board():
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("___|___|___")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("___|___|___")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("   |   |   ")

turn = 0
player = "X"
gameover = False
while True:
    if gameover:
        break
    # repeats the turn
    
    if turn%2 == 0:
        player = "X"
    else:
        player = "O"
    board()
    user_input= input("Enter a number: ")
    i=0
    
    while i<9:
        if cells[i]==int(user_input):
            cells[i]=player
            turn += 1
            break
        i += 1
    

    gameover = find_winner(7, 1, 3)
    gameover = find_winner(3, 3, 1)
    gameover = find_winner(1, 4, 1)

    if cells[2]==cells[4]==cells[6]:
        print("You Win")
        gameover=True

