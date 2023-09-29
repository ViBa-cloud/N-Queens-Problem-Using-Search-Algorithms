#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:38:42 2023

@author: vinayakbassi
"""

from utils import *
import math
import random

def random_state(n=8):
    """Return a random state for n-queens problem."""
    return tuple(random.randint(0, n-1) for _ in range(n))

def simulated_annealing(iterations=100):
    current_state = random_state()
    current_cost = h(current_state)
    h_star = current_cost
    
    for t in range(iterations):
        T = 1 - t/100
        # Choose a column and a row uniformly at random to generate a successor state
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        
        successor = list(current_state)
        successor[col] = row
        
        successor_cost = h(successor)
        
        delta_h = successor_cost - current_cost
        
        # If the new state is better, or with some probability if it's worse
        if delta_h < 0 or (T > 0 and random.random() < math.exp(-delta_h / T)):
            current_state, current_cost = successor, successor_cost
        
        h_star = min(h_star, current_cost)
        
    return h_star

