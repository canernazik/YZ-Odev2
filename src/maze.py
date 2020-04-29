import random


class Maze:
    __obstacle_direction = ['x', 'y']
    
    def __init__(self, row_count, column_count, obstacle_count):
        self.__row_count = row_count
        self.__column_count = column_count
        self.__matrix = [[0 for y in range(column_count)] for x in range(row_count)]
        self.__fill_edges()
        self.__put_obstacles(obstacle_count)
        
        self.__matrix[1][1] = 8
        self.__matrix[self.__row_count - 2][self.__column_count - 2] = 8

        #Todo: Should add the obstacles
        #2 types of obstacles should exist. Vertical or Horizontal.
        #todo: move right, left up, down da eklenmeli

    def __fill_edges(self):
        for i in [0 , self.__row_count - 1]:
            for j in range(0, self.__column_count):
                self.__matrix[i][j] = 1
        
        for j in [0, self.__column_count - 1]:
            for i in range(0, self.__row_count):
                self.__matrix[i][j] = 1
    
    def __put_obstacles(self, obstacle_count):
        ## Obstacle size is 4*1 or 1*4 depending on its direction
        for i in range(obstacle_count):            
            self.__generate_obstacle(4)

    def __generate_obstacle(self, obstacle_length):
        ## Todo: Buraya su kontrol eklenmeli. Obstacle eklenirken ya da en sonunda olusturuldugunda baslangictan bitise gidilebiliyor mu
        ## todo: bunun kontrolunun eklenmesi gerekiyor
        
        can_place_obstacle = False

        while can_place_obstacle == False:
            direction = self.__generate_direction()
            x, y = self.__generate_starting_point(direction)
            can_place_obstacle = self.__validate_obstacle_position(x, y, direction, obstacle_length)
        
        if direction == 'x':
            for j in range(y, y + obstacle_length):
                self.__matrix[x][j] = 1
        else:
            for i in range(x, x + obstacle_length):
                self.__matrix[i][y] = 1

    
    def __generate_direction(self):
        i = random.randint(0,1)
        #print("Direction: " + self.__obstacle_direction[i])
        return self.__obstacle_direction[i]

    def __generate_starting_point(self, direction):        
        x = random.randint(1, self.__row_count - 1)
        y = random.randint(1, self.__column_count - 1)

        return x, y


    def __validate_obstacle_position(self, x, y, direction, obstacle_length):
        if (x == 1 and y == 1) or (x == self.__row_count-2 and y == self.__column_count-2):
            return False
        
        if direction == 'y':            
            if (y == self.__column_count-2) and (x + obstacle_length -1 >= self.__row_count - 2):
                return False
            
            if x + obstacle_length - 1 >= self.__row_count - 1:
                return False

            for i in range(x, x + obstacle_length):
                if self.__matrix[i][y] == 1:
                    return False
        else:            
            if(x == self.__row_count-2) and (y + obstacle_length -1 >= self.__column_count - 2):
                return False
            
            if y + obstacle_length - 1 >= self.__column_count - 1:
                return False
            
            for j in range(y, y + obstacle_length):
                if self.__matrix[x][j] == 1:
                    return False

        return True
    
    def print_matrix(self):
        for i in range(self.__row_count):
            print(''.join(str(x) for x in self.__matrix[i]))
    
    def get_matrix(self):
        return self.__matrix


import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

maze = Maze(20, 100, 100)

maze.print_matrix()
matrix = maze.get_matrix()


# create discrete colormap
cmap = colors.ListedColormap(['white', 'red', 'green'])
bounds = [0,0.9, 5, 10]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(figsize=(25,25))
ax.imshow(matrix, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, len(matrix), 1));
ax.set_yticks(np.arange(-.5, len(matrix), 1));


plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

plt.show()
     