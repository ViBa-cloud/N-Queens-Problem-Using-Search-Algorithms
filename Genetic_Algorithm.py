#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:43:21 2023

@author: vinayakbassi
"""

from utils import *
import math
import random

def random_state(n=8):
    """Return a random state for n-queens problem."""
    return tuple(random.randint(0, n-1) for _ in range(n))



def fitness(state):
    return 28 - h(state)

def select_parent(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for state, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return state

def crossover(parent1, parent2):
    # Choose a crossover point
    crossover_point = random.randint(1, 7) # There are 7 possibilities for crossover points
    child = list(parent1[:crossover_point] + parent2[crossover_point:])
    return child

def mutate(child):
    if random.random() < 0.1:  # 10% mutation rate
        col_to_mutate = random.randint(0, 7)
        new_row = random.randint(0, 7)
        child[col_to_mutate] = new_row
    return child



def genetic_algorithm(iterations=100, pop_size=4):
    population = [random_state() for _ in range(pop_size)]
    h_star = min(h(state) for state in population)
    
    for _ in range(iterations):
        fitnesses = [fitness(state) for state in population]
        
        new_population = []
        for _ in range(pop_size // 2):  # Using // to ensure it's integer division
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
        h_star = min(h_star, min(h(state) for state in population))
        
    return h_star



