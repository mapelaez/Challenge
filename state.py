class State:
    def __init__(self, rod, labyrinth,moves=0):
        self.rod = rod
        self.labyrinth = labyrinth
        self.moves = moves
        self.horizontal_goal_pos = (
            (len(self.labyrinth.matrix) - 1, len(self.labyrinth.matrix[0]) - 3),
            (len(self.labyrinth.matrix) - 1, len(self.labyrinth.matrix[0]) - 2),
            (len(self.labyrinth.matrix) - 1, len(self.labyrinth.matrix[0]) - 1)
        )
        self.vertical_goal_pos = (
            (len(self.labyrinth.matrix) - 3, len(self.labyrinth.matrix[0]) - 1),
            (len(self.labyrinth.matrix) - 2, len(self.labyrinth.matrix[0]) - 1),
            (len(self.labyrinth.matrix) - 1, len(self.labyrinth.matrix[0]) - 1)
        )

    def is_goal(self):
        if tuple(self.rod.positions) == self.horizontal_goal_pos and self.rod.orientation == "H":
            return True
        elif tuple(self.rod.positions) == self.vertical_goal_pos and self.rod.orientation == "V":
            return True
        else:
            return False

    def get_next_states(self):
        next_states = []
        for direction in ["R", "L", "U", "D"]:
            new_rod = self.rod.move(direction, self.labyrinth)
            if new_rod is not None:
                next_states.append(State(new_rod, self.labyrinth, self.moves + 1))
        new_rod = self.rod.rotate(self.labyrinth)
        if new_rod is not None:
            next_states.append(State(new_rod, self.labyrinth, self.moves + 1))
        return next_states

    def heuristic(self):
        distance_horizontal = min(
            abs(self.horizontal_goal_pos[0][0] - self.rod.positions[-1][0]) + abs(self.horizontal_goal_pos[0][1] - self.rod.positions[-1][1]),
            abs(self.horizontal_goal_pos[1][0] - self.rod.positions[-1][0]) + abs(self.horizontal_goal_pos[1][1] - self.rod.positions[-1][1]),
            abs(self.horizontal_goal_pos[2][0] - self.rod.positions[-1][0]) + abs(self.horizontal_goal_pos[2][1] - self.rod.positions[-1][1])
        )
        distance_vertical = min(
            abs(self.vertical_goal_pos[0][0] - self.rod.positions[-1][0]) + abs(self.vertical_goal_pos[0][1] - self.rod.positions[-1][1]),
            abs(self.vertical_goal_pos[1][0] - self.rod.positions[-1][0]) + abs(self.vertical_goal_pos[1][1] - self.rod.positions[-1][1]),
            abs(self.vertical_goal_pos[2][0] - self.rod.positions[-1][0]) + abs(self.vertical_goal_pos[2][1] - self.rod.positions[-1][1])
        )
        return min(distance_horizontal, distance_vertical)

    def __lt__(self, other):
        return self.moves < other.moves