from random import random
from cell import Cell

class Grid():
    def __init__(self, sizex, sizey):
        self.sizex = sizex
        self.sizey = sizey
        self.cells = []
        self.grid = []

    def randomCell(self):
        for i in range(self.sizey):
            for j in range(self.sizex):
                r = random()
                if r >= 0.5:
                    self.cells.append((Cell((j,i), 1)))
                else:
                    self.cells.append((Cell((j,i), 0)))
  
    def random_state(self):
        self.randomCell()
        self.grid = [[[i.state for i in self.cells]] * self.sizex for _ in range(self.sizex)]

    def updateGrid(self):
        for i in self.cells:
            c = i.coor
            self.grid[c[1]][c[0]] = i.state

        
    def displaygrid(self):
        print()
        for i in self.cells:
            if i.state == 0:
                i.state = ' '
            elif i.state == 1:
                i.state = '▉'
        self.updateGrid()
        print('\n'.join(' '.join(map(str,x)) for x in self.grid[::-1]))
        for i in self.cells:
            if i.state == ' ':
                i.state = 0
            elif i.state == '▉':
                i.state = 1

    
    def next_board(self):
        a = [self.surroundingPoints(i) for i in self.cells]        
        for j in a:
            self.checkParam(j)


    def surroundingPoints(self, cell):
        coor = cell.coor
        x = coor[0]
        y = coor[1]
        lcell = []
        for i in self.cells:
          ix = i.coor[0]
          iy = i.coor[1]
          s = i.state
          if (ix == x + 1 and iy == y + 1):
              lcell.append(s)
          elif (ix == x - 1 and iy == y + 1):
              lcell.append(s)
          elif (ix == x + 1 and iy == y - 1):
              lcell.append(s)
          elif (ix == x - 1 and iy == y - 1):
              lcell.append(s)
          elif (ix == x + 1 and iy == y):
              lcell.append(s)
          elif (ix == x - 1 and iy == y):
              lcell.append(s)
          elif (iy == y + 1 and ix == x):
              lcell.append(s)
          elif (iy == y - 1 and ix == x):                
              lcell.append(s)        
            
        return [lcell, cell]

    def checkParam(self, poiCell):
        states = poiCell[0]
        cell = poiCell[1]
        livingcells = sum([i for i in states if i == 1])  
        cstate = self.cells[self.cells.index(cell)]   
        if cell.state == 1 and (livingcells < 2 or livingcells > 3):
            cstate.state = 0
        elif cell.state == 0 and livingcells == 3:
            cstate.state = 1
        elif cell.state == 0 and livingcells == 2:
          if random() > 0.99:
            cstate.state = 1
          else:
            cstate.state = 0
    
def generation(grid):
    while 1:
        grid.next_board()
        grid.displaygrid()
            



grid = Grid(int(input('Length of x axis: ')),int(input('Length of y axis: ')))

grid.random_state()
grid.displaygrid()
generation(grid)
