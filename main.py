import time 
import random

print("Motor Circut Simulation Lab")

results = []

for i in range(10): 

    print("\n----------------------")
    print(f"Trial {i+1}") # the thing that needs to be changed

    # wait before stimmmm pls work 
    time.sleep(random.uniform(1.5, 3))

print("Get ready...")

time.sleep(random.uniform(1, 2))

print("GO!")

start = time.time()
input() # this has to be the user reaction
end = time.time()

rt = end - start
results.append(rt)

print(f"Reaction time: {rt: .3f} seconds")

# hope this pauses before the next trial
print("Next trial starting soon...")
time.sleep(2)

print("\n EXPERIMENT COMPLETE")
print("Average reaction time:", sum(results) / len(results))