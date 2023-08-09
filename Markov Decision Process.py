import matplotlib.pyplot as plt

# Environment
grid = [
    ['fire', None, 'diamond'],
    [None, None, None],
    ['start', None, 'blocked']
]

# Possible actions
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Reward function
reward = {
    'fire': -100,
    'diamond': 100,
    'blocked': -10,
    None: -1,
    'start': 0
}

# Discount factor
gamma = 0.9

# Utility function
utility = {}

# Transition probability function
def transition_probability(state, action, next_state):
    transition_probs = {
        ('start', 'UP', 'fire'): 0.2,
        ('start', 'UP', 'start'): 0.8,
        ('start', 'DOWN', 'start'): 0.2,
        ('start', 'DOWN', 'fire'): 0.8,
        ('start', 'LEFT', 'blocked'): 0.3,
        ('start', 'LEFT', 'start'): 0.7,
        ('start', 'RIGHT', 'diamond'): 1.0,
        (None, None, None): 1.0,  # All other state-action pairs lead to None (no change in state)
        ('diamond', 'UP', 'diamond'): 1.0,  # Terminal state transition (no change in state)
        ('fire', None, None): 1.0,  # Terminal state transition (no change in state)
        ('blocked', None, None): 1.0  # Terminal state transition (no change in state)
    }


    return transition_probs.get((state, action, next_state), 0.0)

# store the iterations and precision values
iteration_list = []
precision_list = []

# optimal policy using Value Iteration
def value_iteration():
    global utility
    iterations = 0
    delta = 1e-4

    while True:
        iterations += 1
        new_utility = utility.copy()
        max_diff = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                state = grid[i][j]
                if state == 'blocked':
                    continue

                max_action_utility = float('-inf')
                for action in actions:
                    next_state = get_next_state(i, j, action)
                    action_utility = 0
                    for next_i in range(len(grid)):
                        for next_j in range(len(grid[0])):
                            next_state = grid[next_i][next_j]
                            reward_value = reward[next_state]
                            transition_prob = transition_probability(state, action, next_state)
                            action_utility += transition_prob * (reward_value + gamma * utility.get((next_i, next_j), 0))

                    max_action_utility = max(max_action_utility, action_utility)

                new_utility[(i, j)] = max_action_utility
                max_diff = max(max_diff, abs(new_utility[(i, j)] - utility.get((i, j), 0)))

        if max_diff < delta:
            break

        utility = new_utility
        iteration_list.append(iterations)
        precision_list.append(max_diff)

        print(f"Iteration {iterations}: Precision = {max_diff:.3f}")

    print(f"Value Iteration converged in {iterations} iterations.")

    # Plot the graph
    plt.plot(iteration_list, precision_list)
    plt.xlabel('Iterations')
    plt.ylabel('Precision (%)')
    plt.title('Precision Convergence During Value Iteration')
    plt.grid()

    # Find the max precision iteration and mark it on the graph with a red dot
    plt.scatter(iterations, 0, color='red', label=iterations)

    plt.legend()
    plt.show()

# get the next state based on the current state and action
def get_next_state(i, j, action):
    if action == 'UP':
        i = max(0, i - 1)
    elif action == 'DOWN':
        i = min(len(grid) - 1, i + 1)
    elif action == 'LEFT':
        j = max(0, j - 1)
    elif action == 'RIGHT':
        j = min(len(grid[0]) - 1, j + 1)

    return grid[i][j]

# test if the desired goal is achieved or not
def goal_achieved():
    return utility.get((0, 2), 0) >= 100

# Run the value iteration to calculate the optimal policy
value_iteration()

# Test if the desired goal is achieved or not
if utility.get((0, 2), 0) >= 100:
    print("The agent achieved the goal of reaching the diamond state.")
else:
    print("The agent did not achieve the goal of reaching the diamond state.")
