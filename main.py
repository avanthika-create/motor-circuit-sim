import time

results = []

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

    # saving part hopefully 

    results.append(reaction_time)

    print(f"Reaction Time: {reaction_time} seconds")

    time.sleep(1)

    print("\n Experiment Complete")

    average = sum(results) / len(results)

    print(f"Average Reaction Time: {average:.3f} seconds")

    print("\nAll Reaction Times:")

    for r in results: 
        print(f"{r:.3f}")