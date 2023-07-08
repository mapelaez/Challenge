class Labyrinth:
    def __init__(self, matrix):
        self.matrix = matrix

    def blocked_pos(self, position):
        x, y = position     
        if  self.pos_in_bounds(position) and self.matrix[x][y] != "#":
            return False
        else:
            return True

    def pos_in_bounds(self, position):
        x, y = position 
        if 0 <= x < (len(self.matrix)) and 0 <= y < (len(self.matrix[0])):
            return True
        else:
            return False
