# import necessary l i b r a r i e s
import numpy as np
import matplotlib . pyplot as plt
# initialization variable
N = 10000
Susceptible = N - 1
Infected = 1
Recovered = 0
beta = 0.3
gamma = 0.05

# Create arrays to track variables
S_array = [Susceptible]
I_array = [Infected]
R_array = [Recovered]

# time loop
for _ in range(1000):
    # Calculate contact probability
    contact_probability = Infected / N
    
    # Susceptible persons were randomly selected to become infected
    for i in range(Susceptible):
        if np.random.rand() < beta * contact_probability:
            Infected += 1
            Susceptible -= 1
    
    # Infected persons were randomly selected to become survivors
    for i in range(Infected):
        if np.random.rand() < gamma:
            Recovered += 1
            Infected -= 1
    
    # Update array
    S_array.append(Susceptible)
    I_array.append(Infected)
    R_array.append(Recovered)
    
plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.plot(I_array,c="blue")
plt.plot(S_array,c="green")
plt.plot(R_array,c="brown")
plt.legend(['Infected','Susceptible','Recovered'])
plt.show()
plt.close()


