import heapq
from  state import State

class Solution:
    def __init__(self, labyrinth, rod):
        self.labyrinth = labyrinth
        self.rod = rod
        self.visited = set()

    def solve(self):
        queue = [(0, State(self.rod, self.labyrinth))]
        while queue:
            _, current_state = heapq.heappop(queue)
            state_key = (tuple(current_state.rod.positions), current_state.rod.orientation)
            if state_key in self.visited:
                continue
            self.visited.add(state_key)
            if current_state.is_goal():
                return current_state.moves  
            for next_state in current_state.get_next_states():
                next_state_key = (tuple(next_state.rod.positions), next_state.rod.orientation)
                if next_state_key not in self.visited:
                    priority = next_state.moves + next_state.heuristic()
                    heapq.heappush(queue, (priority, next_state))
        return -1 

    