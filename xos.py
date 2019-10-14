class NoughtsAndCrosses :
    def __init__(self):
        self.board = [['_'] * 3 for i in range(3)]
        self.won = False

    def display(self):
        for line in self.board:
            print( line[0] + ' | ' + line[1] + ' | '  + line[2] )
        print ("\n")

    def check(self, player):
        for line in self.board: #across
            if all(x == line[0] for x in line) and line[0]!='_':
                print("Player {} you have won! ".format('1' if player else '2'))
                self.won = True
        for x in range(3): #up/down
            if self.board[0][x] == self.board[1][x] == self.board[2][x] and self.board[0][x]!='_':
                print("Player {} you have won! ".format('1' if player else '2'))
                self.won = True
        #diagonals - tidy this
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            print("Player {} you have won! ".format('1' if player else '2'))
            self.won = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            print("Player {} you have won! ".format('1' if player else '2'))
            self.won = True

    def move(self, player, position ):
        symbol = "O" if player else "X"
        if -1 < position < 9:
            if self.board[position//3][position%3] == '_':
                self.board[position//3][position%3] = symbol
                game.display()
                self.check(player)
            else:
                print ("Space taken! ")
                space = int(input("Please select a different space: "))
                self.move(player, space)
        else:
            print("Space out of range! ")
            space = int(input("Please select a different space: "))
            self.move(player, space)


game = NoughtsAndCrosses()
print("Noughts and Crosses \n Player 1 = O, Player 2 = X \n board has 9 squares: 0-8. These are labelled like this: \n 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8")
player = True
while not game.won:
    space = int(input("Player {}, please select your space: ".format('1' if player else '2')))
    game.move( player, space )
    player = not player
