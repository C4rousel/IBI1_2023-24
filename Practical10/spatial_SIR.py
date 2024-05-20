# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
beta = 0.3  # Infection probability per neighbor per time step
gamma = 0.05  # Recovery rate per time step
# make array of all susceptible population
population = np.zeros((100, 100), dtype=int)
# Randomly select the x and y coordinates for the outbreak
outbreak = np.random.choice(range(100), size=2, replace=False)
# Set the status of the selected individual to infected (1)
population[outbreak[0], outbreak[1]] = 1
# Set up the colormap
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(vmin=0, vmax=2)

# Plot the initial state of the population
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap=cmap, norm=norm, interpolation='nearest')
plt.colorbar()
plt.title('Initial State of the 2D SIR Model')
plt.show()
# Function to perform infection and recovery
def update_population(population, beta, gamma):
    # Copy the population to avoid modifying the original array during iteration
    new_population = population.copy()
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:  # Infected
                # Check neighbors and infect with probability beta
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 100 and 0 <= nj < 100 and population[ni, nj] == 0:
                            if np.random.rand() < beta:
                                new_population[ni, nj] = 1
                # Recover with probability gamma
                if np.random.rand() < gamma:
                    new_population[i, j] = 2
    return new_population

# List to store the population state at each time step
population_history = [population]

# Run the simulation for 100 time points
for _ in range(100):
    population = update_population(population, beta, gamma)
    population_history.append(population)

# You can now plot the population state at different time points
# Function to plot the population at a given time step
def plot_population_at_time(population, time_step):
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap=cmap, norm=norm, interpolation='nearest')
    plt.colorbar()
    plt.title(f'Time Step {time_step}')
    plt.show()
    plt.close("Figure 1")

# Plot the model at times 0, 10, 50, and 100
for q in range (0,100,10):
    plot_population_at_time(population_history[q], q)
    plt.close()


