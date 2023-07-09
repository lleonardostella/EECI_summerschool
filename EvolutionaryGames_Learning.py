import numpy as np
import matplotlib.pyplot as plt

def q_learning(payoff_matrix, initial_condition, learning_rate, discount_factor, num_iterations):
    num_strategies = len(payoff_matrix)
    q_table = np.zeros((num_strategies, num_strategies))
    proportions = np.zeros((num_iterations, num_strategies))

    for i in range(num_iterations):
        current_strategy = np.random.choice(range(num_strategies), p=initial_condition)
        opponent_strategy = np.random.choice(range(num_strategies))

        current_payoff = payoff_matrix[current_strategy, opponent_strategy]
        future_strategy = np.argmax(q_table[current_strategy])

        q_table[current_strategy, opponent_strategy] += learning_rate * (current_payoff + discount_factor * q_table[current_strategy, future_strategy] - q_table[current_strategy, opponent_strategy])

        # Calculate proportions at each iteration
        proportions[i] = np.sum(q_table, axis=1) / np.sum(q_table)

    return proportions

# Define the payoff matrix
payoff_matrix = np.array([[3, 0], [5, 1]])

# Define the initial condition
initial_condition = np.array([0.5, 0.5])

# Define the learning rate (alpha)
learning_rate = 0.5

# Define the discount factor (gamma)
discount_factor = 0.9

# Define the number of iterations
num_iterations = 100

# Run Q-learning
proportions = q_learning(payoff_matrix, initial_condition, learning_rate, discount_factor, num_iterations)

# Plot the dynamics
iterations = np.arange(1, num_iterations + 1)

plt.plot(iterations, proportions[:, 0], 'r', label='Cooperators')
plt.plot(iterations, proportions[:, 1], 'b', label='Defectors')
plt.xlabel('Iterations')
plt.ylabel('Proportion')
plt.title('Reinforcement Learning Dynamics: Prisoner\'s Dilemma')
plt.legend()
plt.show()
