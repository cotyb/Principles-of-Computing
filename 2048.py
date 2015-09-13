"""
Clone of 2048 game.
"""
import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048

    """
    # replace with your code
    result_final = []
    result = []
    for dummy_count in range(len(line)):
        result.append(0)
        result_final.append(0)
    index = 0
    for dummy_ele in line:
        if dummy_ele != 0:
            result[index] = dummy_ele
            index += 1
    
    for dummy_count in range(len(result)-1):
        if result[dummy_count] == result[dummy_count+1]:
            result[dummy_count] = 2 * result[dummy_count]
            result[dummy_count+1] = 0
    index = 0        
    for dummy_ele in result:
        if dummy_ele != 0:
            result_final[index] = dummy_ele
            index += 1
            
    return result_final


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height_ = grid_height
        self._grid_width_ = grid_width
        
        self._initial_ = {UP: [(0, i) for i in range(self._grid_width_)],
                  DOWN: [(self._grid_height_-1, i) for i in range(self._grid_width_)],
                  LEFT: [(i, 0) for i in range(self._grid_height_)],
                  RIGHT: [(i, self._grid_width_-1) for i in range(self._grid_height_)]}
        self._iter_num_ = {UP: self._grid_height_,
                   DOWN: self._grid_height_,
                   LEFT: self._grid_width_,
                   RIGHT: self._grid_width_}
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid = [([0] * self._grid_width_) for dummy_i in range(self._grid_height_)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return "chenyajing"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height_

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width_
    
    def add(self, list_l1, list_l2):
        """
        Get the sum of the two lists.
        """
        return [i+j for i,j in zip(list_l1,list_l2)]

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        offset_list = OFFSETS[direction]
        for dummy_list in self._initial_[direction]:
            tmplist = []
            pos = dummy_list
            for dummy_i in range(self._iter_num_[direction]):
                tmplist.append(self.grid[pos[0]][pos[1]])
                pos = self.add(pos, offset_list)
            tmplist = merge(tmplist)
            pos = dummy_list
            for dummy_i in range(self._iter_num_[direction]):
                self.grid[pos[0]][pos[1]] = tmplist[dummy_i]
                pos = self.add(pos, offset_list)
                
        self.new_tile()
                

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        flag = 0
        for dummy_list in self.grid:
            if 0 in dummy_list:
                flag = 1
        if not flag:
            return self.grid
        else:
            pos = [random.randrange(0,self._grid_height_), random.randrange(0,self._grid_width_)]
            if self.grid[pos[0]][pos[1]] == 0:
                random_num = random.randrange(0,11)
                if random_num == 10:
                    self.grid[pos[0]][pos[1]] = 4
                else:
                    self.grid[pos[0]][pos[1]] = 2
            else:
                self.new_tile()
            return self.grid
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 6))
