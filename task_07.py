import random
import matplotlib.pyplot as plt

# Define the number of simulations
num_simulations = 1000000

# Initialize a dictionary to store the count of each sum
sum_counts = {i: 0 for i in range(2, 13)}

# Simulate the dice rolls
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dices = dice1 + dice2
    sum_counts[sum_dices] += 1

# Calculate probabilities
sum_probabilities = {sum_val: count / num_simulations for sum_val, count in sum_counts.items()}

# Display results
print("Sum | Simulated Probability | Theoretical Probability")
print("--- | --------------------- | ---------------------")
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
for sum_val in range(2, 13):
    print(f"{sum_val:2}  | {sum_probabilities[sum_val]:.4%}             | {theoretical_probabilities[sum_val]:.4%}")

# Plotting the results
sums = list(sum_counts.keys())
simulated_probs = [sum_probabilities[sum_val] for sum_val in sums]
theoretical_probs = [theoretical_probabilities[sum_val] for sum_val in sums]

plt.figure(figsize=(10, 5))
plt.bar(sums, simulated_probs, alpha=0.5, label='Simulated Probability', color='blue')
plt.plot(sums, theoretical_probs, marker='o', linestyle='-', color='red', label='Theoretical Probability')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Probability of Sums of Two Dice Rolls')
plt.legend()
plt.grid(True)
plt.show()
