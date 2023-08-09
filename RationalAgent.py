class RationalAgent:
    def __init__(self):
        self.environment = [['A', 'B', 'C', 'D'],
                            ['E', 'F', 'G', 'H'],
                            ['I', 'J', 'K', 'L'],
                            ['M', 'N', 'O', 'P']]
        self.dirt = [[False, False, True, False],
                     [False, True, False, True],
                     [True, False, True, False],
                     [True, False, True, False]]
        self.location = (0, 0)  # Starting location (row, column)
        self.cleaned = [[False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False]]
        self.bag = 0  # Current dirt capacity in the bag
        self.energy = 100  # Initial energy points

    def print_info(self):
        print("Environment:", self.environment)
        print("Dirt:", self.dirt)
        print("Location:", self.location)
        print("Cleaned:", self.cleaned)
        print("Bag:", self.bag)
        print("Energy:", self.energy)

    def clean_dirt(self):
        rows = len(self.environment)
        cols = len(self.environment[0])

        # Traverse and mark each location as checked
        for i in range(rows):
            for j in range(cols):
                self.cleaned[i][j] = True
                self.energy -= 1  # Decrease energy points

                if self.dirt[i][j]:
                    self.bag += 1  # Increase dirt capacity in the bag

        # Update location to the last position
        self.location = (rows - 1, cols - 1)


# ----------------------------------------------------------------#

# agent = RationalAgent()
# agent.print_info()  # Before cleaning
# agent.clean_dirt()
# agent.print_info()  # After cleaning



# ----------------------------------------------------------------#

from collections import deque

class RationalAgent2:
    def __init__(self):
        self.environment = [['A', 'B', 'C', 'D'],
                            ['E', 'F', 'G', 'H'],
                            ['I', 'J', 'K', 'L'],
                            ['M', 'N', 'O', 'P']]
        self.dirt = [[False, False, True, False],
                     [False, True, False, True],
                     [True, False, True, False],
                     [True, False, True, False]]
        self.location = (0, 0)  # Starting location (row, column)
        self.cleaned = [[False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False]]
        self.bag = 0  # Current dirt capacity in the bag
        self.energy = 100  # Initial energy points

    def print_info(self):
        print("Environment:", self.environment)
        print("Dirt:", self.dirt)
        print("Location:", self.location)
        print("Cleaned:", self.cleaned)
        print("Bag:", self.bag)
        print("Energy:", self.energy)

    def move_south(self):
        current_row, current_col = self.location
        next_row = current_row + 1

        if next_row < len(self.environment):
            self.location = (next_row, current_col)
            self.energy -= 1  # Decrease energy points

    def move_east(self):
        current_row, current_col = self.location
        next_col = current_col + 1

        if next_col < len(self.environment[0]):
            self.location = (current_row, next_col)
            self.energy -= 1  # Decrease energy points

    def move_north(self):
        current_row, current_col = self.location
        next_row = current_row - 1

        if next_row >= 0:
            self.location = (next_row, current_col)
            self.energy -= 1  # Decrease energy points

    def move_west(self):
        current_row, current_col = self.location
        next_col = current_col - 1

        if next_col >= 0:
            self.location = (current_row, next_col)
            self.energy -= 1  # Decrease energy points

    def clean_dirt(self):
        rows = len(self.environment)
        cols = len(self.environment[0])
        visited = [[False] * cols for _ in range(rows)]  # Track visited locations

        queue = deque([(0, 0)])  # Initialize the queue with the starting location

        while queue:
            current_row, current_col = queue.popleft()
            self.location = (current_row, current_col)

            self.cleaned[current_row][current_col] = True
            self.energy -= 1  # Decrease energy points

            if self.dirt[current_row][current_col]:
                self.bag += 1  # Increase dirt capacity in the bag
                self.dirt[current_row][current_col] = False  # Mark the position as clean

            visited[current_row][current_col] = True

            # Check and add neighboring positions to the queue
            if current_row < rows - 1 and not visited[current_row + 1][current_col]:
                queue.append((current_row + 1, current_col))
            if current_row > 0 and not visited[current_row - 1][current_col]:
                queue.append((current_row - 1, current_col))
            if current_col < cols - 1 and not visited[current_row][current_col + 1]:
                queue.append((current_row, current_col + 1))
            if current_col > 0 and not visited[current_row][current_col - 1]:
                queue.append((current_row, current_col - 1))

    def charge(self):
        queue = deque([(self.location, [])])  # Initialize the queue with the current location and the path taken
        visited = set()

        
        print("---------going charging-----------")
        print("Energy:", self.energy)

        while queue:
            current_location, path = queue.popleft()
            self.location = current_location

            if self.location == (0, 0):
                self.energy = 100  # Recharge the energy to 100
                print("---------charging done-----------")
                print("Energy:", self.energy)
                return path

            visited.add(self.location)

            # Check and add neighboring positions to the queue
            current_row, current_col = self.location

            if current_row < len(self.environment) - 1:
                next_location = (current_row + 1, current_col)
                if next_location not in visited:
                    queue.append((next_location, path + ['S']))

            if current_row > 0:
                next_location = (current_row - 1, current_col)
                if next_location not in visited:
                    queue.append((next_location, path + ['N']))

            if current_col < len(self.environment[0]) - 1:
                next_location = (current_row, current_col + 1)
                if next_location not in visited:
                    queue.append((next_location, path + ['E']))

            if current_col > 0:
                next_location = (current_row, current_col - 1)
                if next_location not in visited:
                    queue.append((next_location, path + ['W']))

        return None  # No path to charging location found

    def emptyBag(self):
        path_to_charge = self.charge()

        print("---------going to empty bag-----------")
        print("Bag:", self.bag)

        if path_to_charge:
            for direction in path_to_charge:
                if direction == 'S':
                    self.move_south()
                elif direction == 'N':
                    self.move_north()
                elif direction == 'E':
                    self.move_east()
                elif direction == 'W':
                    self.move_west()

            self.bag = 0  # Empty the bag
            print("---------bag empty-----------")
            print("Bag:", self.bag)

    def run(self):
        # before: 
        self.print_info()
        print("---------------------")
        self.clean_dirt()
        self.emptyBag()
        print("---------------------")
        # after: 
        self.print_info()


# ----------------------------------------------------------------#

agent2 = RationalAgent2()
agent2.run()

# ----------------------------------------------------------------#

# Pseudo code

from collections import deque

class RationalAgent3:
    def __init__(self):
        # Environment setup
        self.environment = [['A', 'B', 'C', 'D'],
                            ['E', 'F', 'G', 'H'],
                            ['I', 'J', 'K', 'L'],
                            ['M', 'N', 'O', 'P']]
        self.dirt = [[False, False, True, False],
                     [False, True, False, True],
                     [True, False, True, False],
                     [True, False, True, False]]
        self.location = (0, 0)  # Starting location (row, column)
        self.cleaned = [[False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False],
                        [False, False, False, False]]
        self.bag = 0  # Current dirt capacity in the bag
        self.energy = 100  # Initial energy points


    def  move_south(self): 
        ...
        # This method allows the agent to move down in the environment. 
        # It checks the current row and column where the agent is located. 
        # To move down, it increases the row number by 1. However, before moving, 
        # it checks if there is a row below (within the boundaries of the environment).
        # If there is, the agent updates its location to the new row and keeps the 
        # same column. It also gets a bit tired from moving and loses 1 energy point.

    def  move_east(self): 
        ...
        # This method lets the agent move to the right in the environment. 
        # It checks the current row and column where the agent is located. 
        # To move right, it increases the column number by 1. But before moving,
        # it checks if there is a column to the right (within the boundaries of the 
        # environment). If there is, the
        # agent updates its location to the same row and the new column. 
       #  It also gets a bit tired and loses 1 energy point.

    def  move_north(self): 
        ...
        # This method allows the agent to move up in the environment. 
        # It checks the current row and column where the agent is located. 
        # To move up, it decreases the row number by 1. However, before moving, 
        # it checks if there is a row above (within the boundaries of the environment).
        # If there is, the agent updates its location to the new row and keeps the 
        # same column. It also gets a bit tired from moving and loses 1 energy point.

    def move_west(self): 
        ...
        # This method lets the agent move to the left in the environment. 
        # It checks the current row and column where the agent is located. 
        # To move left, it decreases the column number by 1. But before moving, 
        # it checks if there is a column to the left (within the boundaries of
        # the environment). If there is, the agent updates its location to the 
        # same row and the new column. It also gets a bit tired and loses 1 energy point.

    def clean_dirt(self):
        # Clean the dirt piles in a breadth-first search manner
        # using a queue and track visited locations
        ...

    def charge(self):
        # Find the shortest path to the charging location (0, 0)
        # using a breadth-first search and return the path taken
        ...

    def emptyBag(self):
        # Go back to the charging location and empty the bag
        ...

    def run(self):
        # Run the agent's operations
        self.print_info()
        print("---------------------")
        self.clean_dirt()
        self.emptyBag()
        print("---------------------")
        self.print_info()

    def print_info(self):
        # Print the agent's information
        ...

# ----------------------------------------------------------------#


# Create an instance of the RationalAgent3 class
# agent3 = RationalAgent3()
# agent3.run()

# ----------------------------------------------------------------#