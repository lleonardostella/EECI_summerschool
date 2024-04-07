import numpy as np
import matplotlib.pyplot as plt

def replicator_dynamics(payoff_matrix, initial_condition, num_iterations):
    num_strategies = len(payoff_matrix)
    dynamics = np.zeros((num_iterations, num_strategies))
    dynamics[0] = initial_condition

    for i in range(1, num_iterations):
        fitness = np.dot(payoff_matrix, dynamics[i-1])
        avg_fitness = np.dot(fitness, dynamics[i-1])
        dynamics[i] = dynamics[i-1] * (fitness / avg_fitness)
    return dynamics

# Define the payoff matrix
# payoff_matrix = np.array([[3, 0], [5, 1]]) # prisoner's dilemma
payoff_matrix = np.array([[3, 1], [2, 1]]) # stag hunt

# Define the initial condition
initial_condition = np.array([0.15, 0.85])

# Define the number of iterations
num_iterations = 100

# Run replicator dynamics
dynamics = replicator_dynamics(payoff_matrix, initial_condition, num_iterations)

# Plot the dynamics
cooperators = dynamics[:, 0]
defectors = dynamics[:, 1]

plt.plot(cooperators, 'r', label='Cooperators')
plt.plot(defectors, 'b', label='Defectors')
plt.xlabel('Time: t')
plt.ylabel('State: x')
plt.title('Replicator Dynamics: Prisoner\'s Dilemma')
plt.legend()
plt.show()
