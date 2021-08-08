# Tic Tac Toe Game


## What is Tic Tac Toe? How is it played?

Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid.It is a solved game with a forced draw assuming best play from both players.
In order to win the game, a player must place three of their marks in a horizontal, vertical, or diagonal row.

**Example**:

<img alt="Game of Tic-tac-toe, won by X" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/479px-Tic-tac-toe-game-1.svg.png" decoding="async" width="479" height="56" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/719px-Tic-tac-toe-game-1.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/958px-Tic-tac-toe-game-1.svg.png 2x" data-file-width="479" data-file-height="56">

The following example game is won by the first player, X.


There is no universally agreed rule as to who plays first, but in the convention that X plays first is used.

## How to built tic tac toe game using python

### Step 1:



First we are going to create our game board.We will create a function **print_board()** which we can use everytime we want to print the updated board in the game.


```python
board = [" " for i in range(9)]
print(board)
def print_board():
    row1="| {} | {} | {} |".format(board[0],board[1],board[2])
    row2="| {} | {} | {} |".format(board[3],board[4],board[5])
    row3="| {} | {} | {} |".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
print_board()    
    
```

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    |   |   |   |
    |   |   |   |
    |   |   |   |
    
    

### Step 2:

Now,in the main function,we will first take the input from the player and check whether the input is a valid move or not. If the block that player requests is valid ,we will fill that block else we will ask the user to choose another block.
We will create a function **player_move** which will tells whose turn is either `player 1` or `player 2`.


```python
def player_move(icon):
    if icon =="X":
        number=1
    elif icon =="O":
        number=2
        
    print("Your turn player{}".format(number))
    choice = int(input("Enter your move(1-9): ").strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("Space is already occupied!")
        
```

### Step 3:

Now creating a function **is_victory()** which checks whether someone have won or not. In order to win the game, a player must place three of their marks in a horizontal, vertical, or diagonal row.
There might also be a possibility in which no one wins for that we will create a function **is_draw()** which checks whether there is a tie in the game and will return "Its a draw".


```python
def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or\
      (board[3]==icon and board[4]==icon and board[5]==icon) or\
      (board[6]==icon and board[7]==icon and board[8]==icon) or\
      (board[0]==icon and board[3]==icon and board[6]==icon) or\
      (board[1]==icon and board[4]==icon and board[7]==icon) or\
      (board[2]==icon and board[5]==icon and board[8]==icon) or\
      (board[0]==icon and board[4]==icon and board[8]==icon) or\
      (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True 
    else:
        return False
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break  
    elif is_draw():
        print("Its a draw!")
        break   
        
```

    
    |   |   |   |
    |   |   |   |
    |   |   |   |
    
    Your turn player1
    Enter your move(1-9): 1
    
    | X |   |   |
    |   |   |   |
    |   |   |   |
    
    Your turn player2
    Enter your move(1-9): 2
    
    | X | O |   |
    |   |   |   |
    |   |   |   |
    
    Your turn player1
    Enter your move(1-9): 3
    
    | X | O | X |
    |   |   |   |
    |   |   |   |
    
    Your turn player2
    Enter your move(1-9): 5
    
    | X | O | X |
    |   | O |   |
    |   |   |   |
    
    Your turn player1
    Enter your move(1-9): 8
    
    | X | O | X |
    |   | O |   |
    |   | X |   |
    
    Your turn player2
    Enter your move(1-9): 4
    
    | X | O | X |
    | O | O |   |
    |   | X |   |
    
    Your turn player1
    Enter your move(1-9): 9
    
    | X | O | X |
    | O | O |   |
    |   | X | X |
    
    Your turn player2
    Enter your move(1-9): 6
    
    | X | O | X |
    | O | O | O |
    |   | X | X |
    
    O Wins! Congratulations!
    
