from labyrinth import Labyrinth
from rod import Rod
from solution import Solution

class TestCases:
    def __init__(self):
        self.tests = [
             ([[".",".",".",".",".",".",".",".","."],
              ["#",".",".",".","#",".",".",".","."],
              [".",".",".",".","#",".",".",".","."],
              [".","#",".",".",".",".",".","#","."],
              [".","#",".",".",".",".",".","#","."]], 11),

             ([[".",".",".",".",".",".",".",".","."],
               ["#",".",".",".","#",".",".","#","."],
               [".",".",".",".","#",".",".",".","."],
               [".","#",".",".",".",".",".","#","."],
               [".","#",".",".",".",".",".","#","."]], -1),

             ([[".",".","."],
               [".",".","."],
               [".",".","."]], 2),
            
             ([[".",".",".",".",".",".",".",".",".","."],
               [".","#",".",".",".",".","#",".",".","."],
               [".","#",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".","#",".",".",".",".",".",".",".","."],
               [".","#",".",".",".","#",".",".",".","."],
               [".",".",".",".",".",".","#",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."]], 16)
            ]

    def test_solution(self, labyrinth):
        labyrinth = Labyrinth([list(row) for row in labyrinth])
        rod = Rod()
        solution = Solution(labyrinth, rod)
        return solution.solve()

    def run_tests(self):
        for i, (labyrinth, expected_result) in enumerate(self.tests):
            result = self.test_solution(labyrinth)
            if result == expected_result:
                print(f"Test {i+1} passed.")
            else:
                print(f"Test {i+1} failed: expected {expected_result}, got {result}.")
    
if __name__ == "__main__":
    test_cases = TestCases()
    test_cases.run_tests()