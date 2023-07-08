class Rod:
    def __init__(self, positions = ((0,0),(0,1),(0,2)), orientation = "H"):
        self.positions = positions 
        self.orientation = orientation
        
    def move(self, direction, labyrinth):
        new_positions = tuple()
        if direction == "R":
            for i in range(3):
                new_positions += ((self.positions[i][0], self.positions[i][1] + 1),)
        elif direction == "L":
            for i in range(3):
                new_positions += ((self.positions[i][0], self.positions[i][1] - 1),)
        elif direction == "U":
            for i in range(3):
                new_positions += ((self.positions[i][0] - 1, self.positions[i][1]),)
        elif direction == "D":
            for i in range(3):
                new_positions += ((self.positions[i][0] + 1, self.positions[i][1]),)
        if self.can_move(new_positions,labyrinth):
            return Rod(new_positions, self.orientation)
        else:
            return None

    def rotate(self, labyrinth):
        new_positions = tuple()
        if self.can_rotate(labyrinth):
            if self.orientation == "H":
                self.orientation = "V"
                for i in range(-1,2):
                    new_positions += ((self.positions[1][0] + i, self.positions[1][1]),)
            else:
                self.orientation = "H"
                for i in range(-1,2):
                    new_positions += ((self.positions[1][0], self.positions[1][1] + i),)
            return Rod(new_positions, self.orientation)
        else:
            return None

    def can_move(self, new_positions, labyrinth):
        for pos in new_positions:
            if not labyrinth.pos_in_bounds(pos) or labyrinth.blocked_pos(pos):
                return False
        return True
        
    def can_rotate(self, labyrinth):
        new_positions = tuple()
        if self.orientation == "H":
            for i in range(-1,2):
                new_positions += ((self.positions[1][0] + i, self.positions[1][1]),)
        else:
            for i in range(-1,2):
                new_positions += ((self.positions[1][0], self.positions[1][1] + i),)
        if self.can_move(new_positions,labyrinth):
            return True
        else:
            return False

    