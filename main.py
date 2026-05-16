import time 
import random

print("Motor Circut Simulation Lab")
print("Get ready...")

time.sleep(random.uniform(1,3))

print("GO!")

start = time.time()

input("Press enter as fast as possible!")

end = time.time()

reaction_time = end - start

print("Reaction Time:", round(reaction_time, 3), "seconds")