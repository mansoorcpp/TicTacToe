import pygame

def is_victory(board,icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def Boxes():
    arr = []
    for j in range(3):
        for i in range(3):
            arr.append([i*300,j*300])
    return arr

def drawGrid(screen):
    pygame.draw.line(screen,(0,0,0),[300,0],[300,900],width = 6)
    pygame.draw.line(screen,(0,0,0),(600,0),(600,900),width = 6)
    pygame.draw.line(screen,(0,0,0),(0,300),(900,300),width = 6)
    pygame.draw.line(screen,(0,0,0),(0,600),(900,600),width = 6)

class Box:
    def __init__(self,Position,id):
        self.Coordinate = Position
        self.id = id
        self.length = 300
        self.Empty = True
        self.addingPoint = [self.Coordinate[0] + 120,self.Coordinate[1] + 120]
    def Inside(self,Point):
        if Point[0] >= self.Coordinate[0] and Point[0] <= self.Coordinate[0] + self.length:
            if Point[1] >= self.Coordinate[1] and Point[1] <= self.Coordinate[1] + self.length:
                return True
        else:
            return False



class Game:
    def __init__(self):
        self.tally = -1
        starting_player = input("Who plays first X or O \t")
        if starting_player == "X":
            self.tally = 0
            self.symbol = "X"
        else:
            self.tally = 1
            self.symbol = "O"
        
        self.setGame()
        self.setAnimation()
    def setGame(self):
        self.arr = ['*'] * 9
        self.icon = self.symbol
        self.A = False

    def setAnimation(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 900))
        self.screen.fill("purple")
        self.XImg = pygame.image.load("./X.jpg").convert()
        self.OImg = pygame.image.load("./playO.jpg").convert()
        self.fps = 60
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("TIC-TAC-TOE")
        self.running = True
        self.width = 300
        self.boxes = []
        for id,position in enumerate(Boxes()):
            self.boxes.append(Box(position,id + 1))
    def createVis(self,pos):
        for box in self.boxes:
            if box.Inside(pos):
                if box.Empty == True:
                    box.Empty = False
                    if self.tally % 2 == 0:
                        self.screen.blit(self.XImg,[box.addingPoint[0],box.addingPoint[1]])
                        return box.id
                    else:
                        self.screen.blit(self.OImg,[box.addingPoint[0],box.addingPoint[1]])
                        return box.id
                else:
                    print("Box is already filled")
                    return -1
    
    def isDraw(self):
        for i in self.arr:
            if i == "*":
                return False
        return True
    
    def gameOver(self):
        if (self.isDraw()):
            print("Draw")
            return
        if self.icon == "X":
            print("Player X won")
        elif self.icon == "O":
            print("Player O won")
        if "*" in self.arr:
            print("GameOver")
            return
        

    def playing(self,option):
        if option < 1 or option > 9:
            return
        b = option - 1
        while self.arr[b] != "*":
            print("Already filled pick another box")
        self.arr[b] = self.icon
        self.A = is_victory(self.arr,self.icon)
    
    def play(self,option):
        if self.tally % 2 == 0:
            self.icon = "X"
            self.playing(option)
        else:
            self.icon = "O"
            self.playing(option)

    def run(self):
        while(not self.A and "*" in self.arr and self.running):
            option = -1
            drawGrid(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    option = self.createVis(pos)
                    self.play(option)
                    if(option < 1):
                        self.tally = self.tally
                    else:
                        self.tally += 1
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(self.fps)  # limits FPS to 60
        pygame.quit()
        self.gameOver()


A = Game()
A.run()