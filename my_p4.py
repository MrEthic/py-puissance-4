class Player:

    def __init__(self, name: str, symbol: str = 'X'):
        self.name = name
        self.symbol = symbol

class IA(Player):
    
    def __init__(self, name: str = "IA", symbol: str ='O'):
        super().__init__(name, symbol=symbol)


class Board:

    #Size n*m n ligne m colone
    def __init__(self, n: int = 6, m: int = 7, emptyChar: str = u"\u25A1"):
        self.size = (n, m)
        self.emptyChar = emptyChar
        self.board = self.creatEmptyBoard(n, m)


    def __str__(self) -> str:
        pr = ""
        #Pour chaque ligne :
        for i in range(self.size[0]-1, -1, -1):
            pr += "\t".join([self[j][i] for j in range(self.size[1])]) + "\n" #recup chaque ieme des colones
        return pr

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, key: int) -> list:
        return self.board[self.size[0] - key - 1]

    def __setitem__(self, key, value):
        raise TypeError("'Board' object does not support item assignment, if you want to assign a value at a position (x, y) use : B[x][y] = ?")

    def __copy__(self):
        return Board(self.size[0], self.size[1], self.emptyChar)

    def creatEmptyBoard(self, n: int = 6, m: int = 7) -> list :
        B = [[self.emptyChar for _ in range(n)] for _ in range(m)]
        return B

    def isEmpty(self, l: int, c: int) -> bool:
        return self[c][l] == self.emptyChar

    def playAtAs(self, c: int, player: Player) -> (int, int):
        c -= 1
        if self[c].count(self.emptyChar) == 0:
            return None
        i = self[c].index(self.emptyChar)
        self[c][i] = player.symbol
        return (c, i)

    def checkAt(self, pos: (int, int)) -> bool:
        x, y = pos
        symbol = self[x][y]

        # Check colone
        count = 1
        for i in range(1, self.size[0]-y, 1):
            if self[x][y+i] != symbol:
                break 
            count +=1
        for i in range(1, y+1, 1):
            if self[x][y-i] != symbol:
                break 
            count +=1
        if count >= 4 :
            return True

        # Check ligne
        count = 1
        for i in range(1, self.size[1]-x, 1):
            if self[x+i][y] != symbol:
                break
            count += 1
        for i in range(1, x+1, 1):
            if self[x-i][y] != symbol:
                break
            count += 1
        if count >= 4 :
            return True

        #Check diag haut droit
        count = 1
        amp = min([self.size[0]-y, self.size[1]-x])
        for i in range(1, amp, 1):
            if self[x+i][y+i] != symbol:
                break
            count += 1
        amp = min([x+1, y+1])
        for i in range(1, amp, 1):
            if self[x-i][y-i] != symbol:
                break
            count += 1
        if count >= 4 :
            return True

        #Check diag bas droit
        count = 1
        amp = min([y+1, self.size[1]-x])
        for i in range(1, amp, 1):
            if self[x+i][y-i] != symbol:
                break
            count += 1
        amp = min([x+1, self.size[0]-y])
        for i in range(1, amp, 1):
            if self[x-i][y+i] != symbol:
                break
            count += 1
        if count >= 4 :
            return True

        return False


class Game:

    def __init__(self, p1: Player, p2: Player):
        self.p1 = p1
        self.p2 = p2
        self.board = Board()
        self.activePlayer = self.p1
        self.round = 0
        print(self.board)
        self.playRound()

    def ask(self) -> int:
        print(f"{self.activePlayer.name}, c'est a toi de jouer :")
        rep = -1
        while not rep in range(1, self.board.size[1] + 1):
            rep = input("Choisi une colone où jouer : ")
            try:
                rep = int(rep)
            except:
                print("Verifiez votre entrée")
                rep = -1

        return rep        

    def playRound(self):
        movePos = None
        while (movePos == None):
            c = self.ask()
            movePos = self.board.playAtAs(c, self.activePlayer)
        print(self.board)
        if(self.board.checkAt(movePos)):
            print(f"{self.activePlayer.name} à gagné !")
            return
        self.activePlayer = self.p1 if self.activePlayer == self.p2 else self.p2
        self.playRound()

    #p1 -> max
    #p2 -> min
    def minimax(self, board, lastPos, player: player):
        val = board.checkAt(lastPos)
        if player == self.p1: #maximizing
            value = 0 #float("-inf")
            for i in range(board.size[1]):
                playPos = board.playAtAs(i, player)
                if(playPos != None):
                    nv = 1 if board.checkAt(playPos) else 0


    

        
        




    
P1 = Player("Pierre", "X")
P2 = Player("Paul", "O")

G = Game(P1, P2)

