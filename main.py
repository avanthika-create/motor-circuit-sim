import time

results = []
mode = input("Choose mode (normal / low_dopamine / unstable):")

for i in range(10): 

    print(f"\nTrial {i+1}")

    time.sleep(1)

    print("Get ready...")

    time.sleep(2)
    
    print("GO!")

    start = time.time()

    input("Press Enter NOW")

    end = time.time()

    reaction_time = end - start 

    # dopamine part 
    if mode == "low_dopamine":
        reaction_time += 0.25

    elif mode == "unstable":
        import random
        reaction_time += random.uniform(-0.15, 0.35)

    # saving part hopefully 

    results.append(reaction_time)

    print(f"Reaction Time: {reaction_time} seconds")

    time.sleep(1)

    print("\n Experiment Complete")

    average = sum(results) / len(results)

    fastest = min(results)
    slowest = max(results)

    print(f"Average Reaction Time: {average:.3f} seconds")
    print(f"Fastest Reaction Time: {fastest:.3f} seconds")
    print(f"Slowest Reaction Time: {slowest:.3f} seconds")

    print("\nAll Reaction Times:")

    for r in results: 
        print(f"{r:.3f}")

with open("results.txt", "w") as f: 
    f.write("Motor Circut Simulation Results\n\n")

    for i in enumerate(results):
        f.write(f"Trial {i+1}: {r: .3f} seconds\n")

        avg = sum(results) / len(results)
        f.write(f"\nAverage: {avg:.3f} seconds\n")