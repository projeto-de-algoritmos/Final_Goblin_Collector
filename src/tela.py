import pygame

import networkx as nx

import random

import time

import heapq

import operator

import threading

from pygame.constants import KEYDOWN



try:
    pygame.init()
except:
    print("Erro. Programa não inicializado")


WIDTH = 550
HEIGHT = 600
FPS = 30

telaInicial = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Goblin_Collector")


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255,255,0)

w=20

sair = True
sizeBag = 0

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False

    
    pygame.draw.rect(telaInicial, BLACK, (200, 500, 70, 50), 0)

    pygame.font.init() # you have to call this at the start, 
                    # if you want to use this module.
    myfont1 = pygame.font.SysFont('Arial', 22)
    outraFont = pygame.font.SysFont('Arial', 30)

    textoInicial = myfont1.render('Escolha o peso máximo da mochilha do coletor.', 1, WHITE)
    mais = outraFont.render('+', 1, WHITE)
    menos = outraFont.render('-', 1, WHITE)
    bag = pygame.image.load("../bag.png")
    smallBag = pygame.image.load("../smallBag.png") 
    bigBag = pygame.image.load("../bigBag.png") 

    tamanhoPequeno = myfont1.render('10 kg', 1, WHITE)
    tamanhoMedio = myfont1.render('30 kg', 1, WHITE)
    tamanhoGrande = myfont1.render('50 kg', 1, WHITE)
    coletar = myfont1.render('Coletar', 1, WHITE)

    telaInicial.blit(smallBag,(70,234))
    telaInicial.blit(tamanhoPequeno,(85,335))
    telaInicial.blit(bag,(190,200))
    telaInicial.blit(tamanhoMedio,(230,380))
    telaInicial.blit(bigBag,(360,166))
    telaInicial.blit(tamanhoGrande,(430,405))
    telaInicial.blit(textoInicial,(50,40))
    telaInicial.blit(coletar,(410,510))

    mousePos = pygame.mouse.get_pos()

    if(mousePos[0] > 65 and mousePos[0] < 150 and mousePos[1] > 230 and mousePos[1] < 335 and pygame.mouse.get_pressed() == (1,0,0)):
        sizeBag = 10
        pygame.draw.rect(telaInicial, RED, (65, 230, 85, 100), 0) # 10 kg - fundo vermelho
        pygame.draw.rect(telaInicial, BLACK, (185, 195, 135, 175), 0) # 30 kg - fundo preto
        pygame.draw.rect(telaInicial, BLACK, (355, 160, 195, 245), 0) # 50 kg - fundo preto

    if(mousePos[0] > 185 and mousePos[0] < 320 and mousePos[1] > 195 and mousePos[1] < 370 and pygame.mouse.get_pressed() == (1,0,0)):
        sizeBag = 30
        pygame.draw.rect(telaInicial, BLACK, (65, 230, 85, 100), 0) # 10 kg - fundo preto
        pygame.draw.rect(telaInicial, RED, (185, 195, 135, 175), 0) # 30 kg - fundo vermelho
        pygame.draw.rect(telaInicial, BLACK, (355, 160, 195, 245), 0) # 50 kg - fundo preto

    if(mousePos[0] > 355 and mousePos[0] < 530 and mousePos[1] > 160 and mousePos[1] < 405 and pygame.mouse.get_pressed() == (1,0,0)):
        sizeBag = 50
        pygame.draw.rect(telaInicial, BLACK, (65, 230, 85, 100), 0) # 10 kg - fundo preto
        pygame.draw.rect(telaInicial, BLACK, (185, 195, 135, 175), 0) # 30 kg - fundo preto
        pygame.draw.rect(telaInicial, RED, (355, 160, 195, 245), 0) # 50 kg - fundo vermelho

    if(mousePos[0] > 400 and mousePos[0] < 470 and mousePos[1] > 500 and mousePos[1] < 550 and pygame.mouse.get_pressed() == (1,0,0)):
        sair = False
    pygame.display.update()


tela = pygame.display.set_mode((WIDTH, HEIGHT))
# build the grid
def build_grid(x, y, w):
    x = 0
    y = 0 
    for i in range(1,21):
        x = 20                                                            
        y = y + 20                                                        
        for j in range(1, 21):
            pygame.draw.line(tela, WHITE, [x, y], [x + w, y])           
            pygame.draw.line(tela, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(tela, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(tela, WHITE, [x, y + w], [x, y])           
            x = x + 20                                                    


def up(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x + 1, y - 20 + 1, 19, 39), 0)        
    pygame.display.update()                                              
    #time.sleep(2)

def down(y, x):   
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
    #time.sleep(2)


def left(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x - 20 +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def right(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def colup(y, x, color):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, color, (x + 1, y - 20 + 1, 19, 39), 0)        
    pygame.display.update()                                              
    #time.sleep(2)

def coldown(y, x, color):   
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, color, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
    #time.sleep(2)


def colleft(y, x, color):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, color, (x - 20 +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def colright(y, x, color):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, color, (x +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)

#Random DFS

G = nx.grid_2d_graph(20,20)
#Graph of the mst(edge = 1 means it connects the two nodes)
GMAZE = nx.grid_2d_graph(20,20)
#GMAZED exists to stop negative loops on bellmanford alg(happened when it was GMAZE, a undirected graph)
GMAZED = GMAZE.to_directed()


for (x, y) in GMAZE.edges():
    GMAZE.edges[x, y]['weight'] = 0
    GMAZED.edges[x, y]['weight'] = 0
    GMAZED.edges[y, x]['weight'] = 0

for x in GMAZED.nodes():
    GMAZED.nodes[x]['treasures'] = []

def randUnvisitedNeighbor(vertex):
    unvNeigh = []
    neigh = G[vertex]
    for (x, y) in neigh:
        if G.nodes[(x, y)] != {'visited': 1} :
            unvNeigh.append((x, y))

    if len(unvNeigh) >= 1:
        chosenVertex = random.choice(unvNeigh)

    else:
        chosenVertex = False

    return chosenVertex

def moveCell(vertex, nextVertex):
    (x, y) = vertex
    (x2, y2) = nextVertex

    if x == x2:
        if y < y2:
            #time.sleep(.05)
            right(x, y)
        else:
            #time.sleep(.05)
            left(x, y)
    else:
        if x < x2:
            #time.sleep(.05)
            down(x, y)
        else:
            #time.sleep(.05)
            up(x, y)

def moveCellColor(vertex, nextVertex, color):
    (x, y) = vertex
    (x2, y2) = nextVertex

    if x == x2:
        if y < y2:
            time.sleep(.15)
            colright(x, y, color)
        else:
            time.sleep(.15)
            colleft(x, y, color)
    else:
        if x < x2:
            time.sleep(.15)
            coldown(x, y, color)
        else:
            time.sleep(.15)
            colup(x, y, color)

#Instead of iterating through the neigbors it chooses one randomly
def randomDFS(vertex):
    G.nodes[vertex]['visited'] = 1
    nextVertex = randUnvisitedNeighbor(vertex)

    while nextVertex:
        mazecolorint = random.randint(0, 19)
        if mazecolorint < 19:
            mazecolorint = 1
        if mazecolorint == 19:
            mazecolorint = random.randint(-5,5)
            if mazecolorint == 0:
                mazecolorint = 1
        
        GMAZE.edges[vertex, nextVertex]['weight'] = mazecolorint
        mazecolor = GREEN #Normal path
        moveCellColor(vertex, nextVertex, mazecolor)
        randomDFS(nextVertex)
        nextVertex = randUnvisitedNeighbor(vertex)

def addLoopsToMaze():
    count = 0
    ant = -1
    for (u, v) in GMAZE.edges():
        if GMAZE.edges[u, v]['weight'] != 0:
            if ant != u:
                count = 0
            count = count + 1
            ant = u
            if count == 3 and random.randint(0,19)==19:
                count = 0
                GMAZE.edges[u, v]['weight'] = 1
    
#Shortcuts and Obstacles print
def printShOb():
    for (u, v) in GMAZE.edges():
        if GMAZE.edges[u, v]['weight'] < 1 and GMAZE.edges[u, v]['weight'] != 0 :
                pygame.draw.circle(tela, BLUE, [20*(u[1]+v[1])/2 + 30, 20*(u[0]+v[0])/2 + 30], 5) #Obstacle
        if GMAZE.edges[u, v]['weight'] > 1 and GMAZE.edges[u, v]['weight'] != 0:
                pygame.draw.circle(tela, RED, [20*(u[1]+v[1])/2 + 30, 20*(u[0]+v[0])/2 + 30], 5) #Shortcuts
        
#MST MAZE////
def randomEdgesWeight():
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(0,100)
#=====================================================================================
def Prim():
    h = []
    s = []
    a = []
    i =0
    rep=-1
    temp = []
    for (x, y) in G.nodes():
        a.append(101)
        heapq.heappush(h, (a[20*x + y], (x, y)))

    while(h != []):
        heapq.heapify(h)
        u = heapq.heappop(h)
        if rep == -1:
            u = (0, (0,0))
        if rep != -1:
            for (x, y) in G[u[1]]:
                if (x ,y) in s:
                    temp.append((x, y))

            lesser = -1
            lesserxy = 0
            for (x, y) in temp:
                if lesser < a[20*x + y]:
                    lesser = a[20*x + y]
                    lesserxy = (x, y)
            mazecolorint = random.randint(0, 19)
            if mazecolorint < 19:
                mazecolorint = 1
            if mazecolorint == 19:
                mazecolorint = random.randint(-5,5)
                if mazecolorint == 0:
                    mazecolorint = 1
            #GMAZED exists to stop negative loops on bellmanford alg(happened when it was GMAZE, a undirected graph)
            GMAZE.edges[u[1], lesserxy]['weight'] = mazecolorint
            GMAZED.edges[u[1], lesserxy]['weight'] = mazecolorint
            if mazecolorint < 0:
                GMAZED.edges[lesserxy, u[1]]['weight'] = -mazecolorint
            else:
                GMAZED.edges[lesserxy, u[1]]['weight'] = mazecolorint
            mazecolor = GREEN #Normal path
            moveCell(u[1], lesserxy)
            temp = []

        rep = 1
        s.append(u[1])
        neigh = G[u[1]]
        for (x, y) in neigh:
            if (x, y) not in s:
                if G.edges[u[1],(x, y)]['weight'] < a[20*x + y]:
                    a[20*x + y] = G.edges[u[1],(x, y)]['weight']
                    for i in range(len(h)):
                        if h[i][1] == (x, y):
                            h[i] = (a[20*x + y], (x, y))      
                            break          
#====================================================================================
#ShortestPath Divide and Conquer
def DCShortestPath(N, xo, yo, xd, yd, xf, yf, contr, distance=0, curCol = RED):
    if xd > xf or yd > yf:
        return 400
    
    if xd < 0 or yd < 0:
        return 400

    if xo > xf or yo > yf:
        return 400
    
    if xo < 0 or yo < 0:
        return 400
    
    if (xo != xd or yo != yd) and GMAZE.edges[(xo, yo),(xd, yd)]['weight'] == 0:
        return 400

    else:
        if xd == 19 and yd == 19:
            moveCellColor((xo, yo),(xd, yd), BLUE) 
            return distance

        if contr == -1:
            return min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1, RED), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1, RED), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1, RED), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1, RED))    
        
        if contr == 0:
            moveCellColor( (xd, yd),(xo, yo), curCol)
            zmark=min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1, curCol), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1, curCol), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1, curCol))
            if zmark != None and zmark <400:
                moveCellColor((xd, yd),(xo, yo), BLUE)
            return zmark   

        if contr == 1:
            moveCellColor((xo, yo), (xd, yd), curCol)
            onemark =min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1, curCol), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1, curCol), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1, curCol))
            if onemark != None and onemark <400:
                moveCellColor((xd, yd),(xo, yo), BLUE)
            return onemark
        if contr == 2:

            moveCellColor((xo, yo), (xd, yd), curCol)
            twomark = min(DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1, curCol), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1, curCol), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1, curCol))
            if twomark != None and twomark <400:
                moveCellColor((xd, yd),(xo, yo), BLUE)
            return twomark
        if contr == 3:

            moveCellColor((xo, yo), (xd, yd), curCol)
            threemark = min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1, curCol), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1, curCol), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1, curCol))
            if threemark != None and threemark <400:
                moveCellColor((xd, yd),(xo, yo), BLUE)
            return threemark

#================================================================================================
#Shortest Path BellmanFord
def PDBellmanFord(t):
    m = [None] * GMAZED.number_of_nodes()
    sucessor = [None] * GMAZED.number_of_nodes()
    valch= 0
    for x in GMAZED.nodes:
        m[x[0]*20 + x[1]] = 9999
        sucessor[x[0]*20 + x[1]] = 0

    m[t[0]*20 + t[1]] = 0

    for i in range(1 ,GMAZED.number_of_nodes()):
        for x in GMAZE.nodes():
            for y in GMAZE.adj[x]:
                if GMAZED.edges[x, y]['weight'] != 0:
                    if m[x[0]*20 + x[1]] > m[y[0]*20 + y[1]] + GMAZED.edges[x, y]['weight']:
                        m[x[0]*20 + x[1]] = m[y[0]*20 + y[1]] + GMAZED.edges[x, y]['weight']
                        sucessor[x[0]*20 + x[1]] = y
                        valch = 1
        
        if valch == 1:
            valch = 0
        else:
            break

    return [sucessor, m]

#================================================================================================
#GOBLIN COLLECTOR BOT
copiatela = None #screen copy to avoid tracks from the image
avaliableTreasures = [] #list with the treasures avaliable for picking ((pos),(w),(v))
randomGenTreasures = [] #list with the random treasures
rgtSem = threading.Semaphore() #semaphores to avoid colision on threads
telaSem = threading.Semaphore()
mazeSem = threading.Semaphore()
botTreasure = [] #treasure on the possession of the bot
botknap = [] #treasures expected to be colected
bot = None
botpos = None
goblinBoost = 0

def randTreasure(): #generate random treasures
    w=0
    wt=0
    vt=0
    treasures = []
    posx = 0
    posy = 0
    global avaliableTreasures
    rgtSem.acquire()
    while w<50:#maximum total weight of the treasures
        wt = random.randint(1, 5)
        vt = random.randint(1, 25)
        w += wt
        posx = random.randint(1, 19)
        posy = random.randint(1, 19)
        while (posx, posy) in treasures and len(GMAZED.nodes[(posx, posy)]['treasures'])!=0: #supesed to pick a diferent coordinate per treasure
            posx = random.randint(1, 19)
            posy = random.randint(1, 19)
        telaSem.acquire()
        pygame.draw.circle(tela, YELLOW, [20*posy +30, 20*posx +30], 5) #drawn the circle representing the treasure on the maze
        telaSem.release()
        mazeSem.acquire()
        GMAZED.nodes[(posx, posy)]['treasures'].append([wt, vt]) #put the treasure on the maze properties on the formar [w, v](its actually a list [[w,v], ...])
        mazeSem.release()
        treasures.append(((posx, posy),(wt),(vt))) 
        avaliableTreasures.append(((posx, posy),(wt),(vt))) #mark treasure as avaliable
    rgtSem.release()
    return treasures #return the list with the treasures [((pos),(w),(v)),((pos),(w),(v)), ...]


def PDKnapsack(treasures, weight):#knapsack function that returns a list of treasures [((pos),(w),(v)),((pos),(w),(v)), ...]
    m = []
    treasuresonbag = []

    for n in range (0, len(treasures)+1):#initialized this way because weird bug
        m.append([])
        for w in range (0, weight+1):
            m[n].append(0)
    
    for i in range(1, len(treasures)+1):
        for w in range(1, weight+1):
            if treasures[i-1][1] > w:
                m[i][w] = m[i-1][w]
            else:
                m[i][w] = max(m[i-1][w], treasures[i-1][2] + m[i-1][w - treasures[i-1][1]])
        
    tot = m[len(treasures)][weight] #algorithm to get the itens selected ref:https://www.geeksforgeeks.org/printing-items-01-knapsack/
    w = weight
    for i in range(len(treasures), 0, -1):
        if tot == 0:
            break
        
        if tot == m[i-1][w]:
            
            continue
        else:
            treasuresonbag.append(treasures[i-1])
            tot -= treasures[i-1][2]
            w -= treasures[i-1][1]
    
    return treasuresonbag

def goblinMover(prevpos, pos):#function used to move the goblin sprite
    global goblinBoost

    if prevpos != pos:
        global copiatela
        telaSem.acquire()
        tela.blit(copiatela, (0,0))#this is done because we dont want tracks
        goblin = pygame.image.load("../goblin.png").convert_alpha()
        tela.blit(goblin, pos)
        pygame.display.update()
        telaSem.release()
        if GMAZED.edges[prevpos, ((pos[1]-20)/20, (pos[0]-20)/20)]['weight'] > 1:
            goblinBoost += GMAZED.edges[prevpos, ((pos[1]-20)/20, (pos[0]-20)/20)]['weight']
        elif GMAZED.edges[prevpos, ((pos[1]-20)/20, (pos[0]-20)/20)]['weight'] < 1:
            goblinBoost += GMAZED.edges[prevpos, ((pos[1]-20)/20, (pos[0]-20)/20)]['weight']
        
        if goblinBoost > 0:
            time.sleep(1.5)
            goblinBoost -= 1
        if goblinBoost == 0:
            time.sleep(0.5)
        if goblinBoost < 0:
            goblinBoost += 1
            time.sleep(0.1)
        
        

#this is actually a very naive version of the Traveling Salesman Problem, where we seek the shortest route from start to finish through certain point
def recursiveClosest(actualPos, possibleNextPositions):#function were the closest treasure on botknap is found then picked by the goblin who moves on the maze
    minval = 999
    minpos = None
    minall = None
    global copiatela
    global avaliableTreasures
    global bot
    global botTreasure
    global botknap
    global botpos
    global randomGenTreasures

    if possibleNextPositions[0][1] == None :#in case there are no more possible next positions(based on botknap) it moves the goblin to the start/exit
        minalzeroflag = 0
        (x1, y1) = actualPos
        i = 1
        zerozero = PDBellmanFord((0,0))
        while i> 0:
            i = i+1
            (x, y) = zerozero[0][x1*20 + y1]
            goblinMover((x1, y1),(20*y+20, 20*x+20))
            x1 = x
            y1 = y
            if (x, y) == (0, 0):
                break
        return  zerozero[1][actualPos[0]*20 + actualPos[1]]
    for x  in possibleNextPositions:#finds the closest item
        if x[1] == None or x[1] == 0:
            break
        if minval > x[0][1][actualPos[0]*20 + actualPos[1]]:
            minval = x[0][1][actualPos[0]*20 + actualPos[1]]
            minpos = x[1]
            minall = x
    if minall == None:
        print(botknap)
        print(botTreasure)
        print(randomGenTreasures)

    (x1, y1) = actualPos
    i = 1
    while i> 0:#where the goblin is moved through the sucessor matrix obtained with bellmanford
        for xt  in possibleNextPositions: # in case of multiple threads. this exists to detect if a item on the botknap was collected, if so, it creates a new thread and kills the other
            if xt[1] == None:
                break
            if (xt[1],xt[2][0],xt[2][1]) not in avaliableTreasures:#check if the item wanted exists on avaliableTreasure if not it will check if there are itens in bottreasure that do not exist on the new botknap(expected itens)
                knp = PDKnapsack(avaliableTreasures, 20)
                if botTreasure not in knp:
                    botknap = knp
                    for xt2 in botTreasure:
                        if xt2 not in knp:# if there are itens that are not needed on the new botknap they are discarded on the location, and made avaliable
                            botTreasure.remove(xt2)
                            mazeSem.acquire()
                            GMAZED.nodes[(x1,y1)]['treasures'].append([xt2[1], xt2[2]])
                            mazeSem.release()
                            rgtSem.acquire()
                            avaliableTreasures.append(((x1,y1),(xt2[1]),(xt2[2])))
                            rgtSem.release()
                            telaSem.acquire()
                            tela.blit(copiatela, (0,0))
                            pygame.draw.circle(tela, WHITE, [20*y1 +30, 20*x1 +30], 5)#treasures deposited on the white mark
                            copiatela = tela.copy()
                            telaSem.release()
                    botpos = (x1, y1)#this is needed to remember the current position on the maze so that the new thread starts there
                    bot = threading.Thread(target=veryNaiveTPS, args = (knp,)) #then a new thread is created to guide the goblin towards the new treasures
                    bot.start()
                    return 'destroy' #destroy the thread
                
        i = i+1
        (x, y) = minall[0][0][x1*20 + y1]
        goblinMover((x1, y1),(20*y + 20, 20*x + 20)) #moves the goblin one block
        x1 = x
        y1 = y
        if (x, y) == minpos:
            if len(GMAZED.nodes[(x, y)]['treasures']) > 1: #in case there are more than one wanted treasures on the same block
                for xx in botknap:
                    if xx[0] == (x, y):
                        botTreasure.append(xx)
                        GMAZED.nodes[(x, y)]['treasures'].remove([xx[1],xx[2]])
                        if xx in avaliableTreasures:
                            avaliableTreasures.remove(xx)
                        for yy in possibleNextPositions:
                            if xx[0] == yy[1] and yy[2] == [xx[1],xx[2]]:
                                possibleNextPositions.remove(yy)

                        

            else:#if theres only one treasure on the block
                mazeSem.acquire()
                GMAZED.nodes[(x, y)]['treasures'].remove(minall[2])
                mazeSem.release()
                rgtSem.acquire()
                botTreasure.append((minall[1], (minall[2][0]), (minall[2][1])))
                if (minall[1], (minall[2][0]), (minall[2][1])) in avaliableTreasures:
                    avaliableTreasures.remove((minall[1], (minall[2][0]), (minall[2][1])))
                    
                    rgtSem.release()
                mazeSem.acquire()
                possibleNextPositions.remove(minall)
            if len(GMAZED.nodes[(x, y)]['treasures']) == 0:#if there are no more treasures on the block the gold is deleted from the maze
                telaSem.acquire()
                tela.blit(copiatela, (0,0))
                pygame.draw.circle(tela, GREEN, [20*y +30, 20*x +30], 5)
                copiatela = tela.copy()
                telaSem.release()
            mazeSem.release()
            rgtSem.release()
            break
    destroy = recursiveClosest(minpos,possibleNextPositions) #if the return is destroy, it will keep returning destroy until it ends
    if destroy == 'destroy':
        return 'destroy'

    return minval + destroy #this return is actually the weigthed distance

def veryNaiveTPS(treasureinf):# Naive tsp, we collect the weighted distance between the goblin and the treasures and use that information to move to the closest one
    global copiatela
    global botknap
    global botpos
    global sair
    botknap = treasureinf
    telaSem.acquire()
    copiatela = tela.copy()
    telaSem.release()
    

    sucsandval=[[[[], []], None, None] for  i in range (100)]
    i = 0
    for x in treasureinf:#here the distance between treasures and the start/exit and the distance between treasures is calculated
        sucsandval[i][0] = PDBellmanFord(x[0])
        sucsandval[i][1] = x[0]
        sucsandval[i][2] = [x[1], x[2]]
        i = i + 1

    print(recursiveClosest(botpos, sucsandval))
    print(botTreasure)

def createMaze():
    startVertex = (0, 0)
    randomDFS(startVertex)

def playerSimul():#suposed to simulate player interaction with the maze(collecting itens)
    global avaliableTreasures
    global rgtSem
    global copiatela

    
    while 1:
        time.sleep(2)
        rgtSem.acquire()
        pos = avaliableTreasures.pop()
        rgtSem.release()
        telaSem.acquire()
        tela.blit(copiatela, (0,0))
        pygame.draw.circle(tela, PURPLE, [20*pos[0][1] +30, 20*pos[0][0] +30], 5)
        copiatela = tela.copy()
        pygame.display.update()
        telaSem.release()
    


build_grid(40, 0, 20) 
#createMaze()
randomEdgesWeight()
Prim()
addLoopsToMaze()
printShOb()
randomGenTreasures = randTreasure()
knp = (PDKnapsack(randomGenTreasures, sizeBag))
botpos = (0, 0)
bot = threading.Thread(target=veryNaiveTPS, args = (knp,))
player = threading.Thread(target=playerSimul,)
bot.start()
#player.start()
bot.join()
#player.join()



while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    
    pygame.draw.rect(tela, BLACK, (200, 500, 70, 50), 0)
    

    pygame.font.init() # you have to call this at the start, 
                    # if you want to use this module.
    myfont = pygame.font.SysFont('Arial', 22)

    sair = myfont.render('Sair', 1, WHITE)

    tela.blit(sair,(210,510))

    mousePos = pygame.mouse.get_pos()
    #mouse = pygame.mouse.get()

    if(mousePos[0] > 200 and mousePos[0] < 270 and mousePos[1] > 500 and mousePos[1] < 550 and pygame.mouse.get_pressed() == (1,0,0)):
        sair = False
    pygame.display.update()

pygame.quit()