#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:34:15 2023

@author: vinayakbassi
"""

from utils import *
import random



def steepest_descent_hill_climbing(initial_state):
    current_state = initial_state
    current_cost = h(current_state)
    steps = 0

    while True:
        neighbors = []

        # Generate all neighbors by moving each queen in its column
        for col in range(len(current_state)):
            for row in range(len(current_state)):
                if row != current_state[col]:
                    new_state = list(current_state)
                    new_state[col] = row
                    neighbors.append((new_state, h(new_state)))

        # Sort neighbors by cost
        neighbors.sort(key=lambda x: x[1])

        # If the best neighbor is no better than the current state, stop
        if neighbors[0][1] >= current_cost:
            break

        current_state = neighbors[0][0]
        current_cost = neighbors[0][1]
        steps += 1

    return current_state, current_cost, steps




def random_state(n=8):
    """Return a random state for n-queens problem."""
    return tuple(random.randint(0, n-1) for _ in range(n))

def random_restart_steepest_descent_hill_climbing(restarts_limit=100):
    for _ in range(restarts_limit):
        initial = random_state()
        final_state, final_cost, _ = steepest_descent_hill_climbing(initial)
        
        if final_cost == 0:
            return final_state, final_cost

    return final_state, final_cost




def random_restart_steepest_descent_hill_climbing_detailed(restarts_limit=100):
    total_steps = 0
    for i in range(restarts_limit):
        initial = random_state()
        _, final_cost, steps = steepest_descent_hill_climbing(initial)
        total_steps += steps

        if final_cost == 0:
            return i+1, total_steps

    return i+1, total_steps



