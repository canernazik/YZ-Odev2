import random

from point import Point

class Maze:
    __obstacle_direction = ['x', 'y']
    
    def __init__(self, row_count, column_count, obstacle_count):
        self.__row_count = row_count
        self.__column_count = column_count
        self.__starting_point = Point(1, 1)
        self.__finishing_point = Point(row_count-1, column_count-1)
        self.__current_point = Point(1, 1)
        self.__matrix = [[0 for y in range(column_count)] for x in range(row_count)]
        self.__fill_edges()
        self.__put_obstacles(obstacle_count)

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
            can_place_obstacle = self.__validate_obstacle_position(x, y, obstacle_length)
        
        if direction == 'x':
            for j in range(y, y + obstacle_length):
                self.__matrix[x][j] = 1
        else:
            for j in range(x, x + obstacle_length):
                self.__matrix[x][j] = 1

    
    def __generate_direction(self):
        i = random.randint(0,1)
        return self.__obstacle_direction[i]

    def __generate_starting_point(self, direction):        
        is_valid = False

        if direction == 'y':
            max_x = self.__row_count - 4
            max_y = self.__column_count
        else:
            max_x = self.__row_count
            max_y = self.__column_count - 4

        while is_valid == False:
            x = random.randint(1, max_x)
            y = random.randint(1, max_y)

            if x != 1 or y != 1:
                is_valid = True
        
        return x, y


    def __validate_obstacle_position(self, x, y, direction, obstacle_length):
        if direction == 'y':
            if y + obstacle_length >= self.__row_count - 1:
                return False

            for j in range(y, y + obstacle_length):
                if self.__matrix[x][j] == 1:
                    return False
        else:
            if x + obstacle_length >= self.__column_count - 1:
                return False
            
            for j in range(x, x + obstacle_length):
                if self.__matrix[i][y] == 1:
                    return False

        return True            