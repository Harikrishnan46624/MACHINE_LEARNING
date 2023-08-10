import numpy as np

# Define the grid-world environment
grid = np.array([
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 1],
])

# Initialize the Q-table with zeros
q_table = np.zeros((5, 5, 4))  # 5x5 grid with 4 actions (up, down, left, right)

# Set hyperparameters
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 1000

# Q-learning algorithm
for episode in range(num_episodes):
    state = (0, 0)  # Starting state
    done = False

    while not done:
        current_state = state

        # Choose an action using the epsilon-greedy policy
        if np.random.rand() < 0.1:
            action = np.random.randint(4)  # Exploration: random action
        else:
            action = np.argmax(q_table[state])  # Exploitation: choose action with maximum Q-value

        # Simulate taking the selected action and observe the next state and reward
        if action == 0:  # Up
            next_state = (state[0] - 1, state[1])
        elif action == 1:  # Down
            next_state = (state[0] + 1, state[1])
        elif action == 2:  # Left
            next_state = (state[0], state[1] - 1)
        elif action == 3:  # Right
            next_state = (state[0], state[1] + 1)

        # Check if the next state is within the grid boundaries
        if 0 <= next_state[0] < grid.shape[0] and 0 <= next_state[1] < grid.shape[1]:
            reward = grid[next_state]

            # Update the Q-value of the current state-action pair
            q_table[current_state][action] += learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[current_state][action])

            state = next_state

            if reward == 1:
                done = True
        else:
            # If the next state is out of bounds, penalize the agent and end the episode
            reward = -10
            q_table[current_state][action] += learning_rate * (reward - q_table[current_state][action])
            done = True

# Print the learned Q-table
print(q_table)