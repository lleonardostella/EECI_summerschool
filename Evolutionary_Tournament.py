import numpy as np
import matplotlib.pyplot as plt
import random as rand

# Initialising time horizon
T = rand.randrange(100, 1000, 1)

# Creating the arrays of moves, 0 = hare, 1 = stag, 2 = first move
move1 = np.zeros(T, dtype=int)
move2 = np.zeros(T, dtype=int)

# Define the payoff matrix
payoff_matrix = np.array([[4, 1], [3, 2]])

""" TESTING
def stag_hunt1(move):
    if move == 2:
        return 1
    elif move == 1:
        return 1
    else:
        return 0

def stag_hunt2(move):
    if move == 2:
        return 1
    else:
        return 0

def stag_hunt3(move):
    if move == 2:
        return 1
    else:
        return 1
"""

def tik_tok(x):
    if x==2:
        return 1
    else:
        return x
    
def JE_strategy(x):
   if x == 2:
       return 0
   elif x == 1:
       return 1
   elif x == 0:
       return 0

def strategy_RAP(opponent_action):
   if opponent_action == 2:
       return 1
   if opponent_action == 0:
       if rand.uniform(0,1) >= 0.5:
           return 0
       else:
           return opponent_action    
   else:
       if rand.uniform(0,1) >= 0.5:
           return 0
       else:
           return opponent_action
    
def select_strategy(previous_str):
   if (previous_str == 2):
       return rand.choice([0, 1])
   else:
       return previous_str
   
def maximise(input):
    if input == 2:
        return 1
    elif input == 0:
        return 0
    else:
        return 1



stag_hunts = [tik_tok, JE_strategy, strategy_RAP, select_strategy, maximise]
# for func in list_of_functions:
#    func()
N = len(stag_hunts)

# Creating an array of integers of size N (\in \mathbb Z)
p = np.zeros((N, T), dtype=int)

for i in range(0,N-1):
    for j in range(i+1,N):
        move1[0] = stag_hunts[i](2)
        move2[0] = stag_hunts[j](2)

        p[i,0] = p[i,0] + payoff_matrix[move1[0],move2[0]]
        p[j,0] = p[j,0] + payoff_matrix[move2[0],move1[0]]

        for t in range(1,T):
            move1[t] = stag_hunts[i](move2[t-1])
            move2[t] = stag_hunts[j](move1[t-1])

            p[i,t] = p[i,t-1] + payoff_matrix[move1[t],move2[t]]
            p[j,t] = p[j,t-1] + payoff_matrix[move2[t],move1[t]]

        if j != N-1:
            p[i,0] = p[i,T-1]
        if i != N-2:
            p[j,0] = p[j,T-1]

    
print('The number of rounds for this tournament is: ',T)
for i in range(0,N):
    print('The total payoff of player ', i+1, ' is ', p[i,T-1])
    plt.plot(p[i,:], label='Player '+str(i+1))

plt.xlabel('Iteration: t')
plt.ylabel('Cumulative Payoff: x')
plt.title('Evolutionary Tournament: Prisoner\'s Dilemma')
plt.legend()
plt.grid()
plt.show()