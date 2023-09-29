#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:36:16 2023

@author: vinayakbassi
"""
from utils import *
from Hill_climbing import *
from Genetic_Algorithm import *
from Simulated_Annealing import *


#### Solve for Part A

print ("Solution: Part A")
# Provided initial state
initial_state = (7, 3, 1, 0, 2, 5, 4, 1)
final_state, final_cost, steps = steepest_descent_hill_climbing(initial_state)

# a. What is the cost of the initial state?
print("a. Cost of the initial state:", h(initial_state))

# b. What is the final state after the algorithm terminates?
print("b. Final state after the algorithm terminates:", final_state)

# c. Was a solution found? What is the cost of the final state?
print("c. Was a solution found?", final_cost == 0)
print("d. Cost of the final state:", final_cost)

# d. What is the number of steps taken (in the environment) to reach that final state?
print("e. Number of steps taken to reach the final state:", steps)



#### Solve for Part B
print ("Solution: Part B")

final_state, final_cost = random_restart_steepest_descent_hill_climbing()

# B. For the random restart steepest-descent hill climbing,
# a. Was a solution found?
print("a. Was a solution found?", final_cost == 0)

# b. What is the cost of the final state?
print("b. Cost of the final state:", final_cost)


#### Solve for Part C
print ("Solution: Part C")

random.seed(2000)  # Setting the seed

# Run the algorithm 1000 times
total_restarts = 0
total_steps = 0
runs = 1000

for _ in range(runs):
    restarts, steps = random_restart_steepest_descent_hill_climbing_detailed()
    total_restarts += restarts
    total_steps += steps

# Compute empirical estimates
expected_restarts = total_restarts / runs
expected_steps = total_steps / runs

print("a. Expected number of restarts required to find a solution:", expected_restarts)

print("b. Expected total number of steps across restarts required to find a solution:", expected_steps)


#### Solve for Part D
print ("Solution: Part D")
# Run the algorithm 10000 times
h_star_values = [simulated_annealing() for _ in range(10000)]

# Compute the empirical average of h_star
average_h_star = sum(h_star_values) / len(h_star_values)
print("Empirical average of h* across all 10000 runs:", average_h_star)


#### Solve for Part E
print ("Solution: Part E")

# Run the algorithm 10000 times
h_star_values = [genetic_algorithm() for _ in range(10000)]

# Compute the empirical average of h_star
average_h_star = sum(h_star_values) / len(h_star_values)
print("Empirical average of h* across all 10000 runs:", average_h_star)








