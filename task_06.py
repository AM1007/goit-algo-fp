# Define the items with their cost and calories
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100  # Define the budget

# Greedy algorithm to maximize calories per cost ratio
def greedy_algorithm(items, budget):
    # Sort items by the ratio of calories to cost in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0  # Initialize total calories
    total_cost = 0  # Initialize total cost
    selected_items = []  # List to store selected items
    
    # Iterate over the sorted items
    for item, details in sorted_items:
        # Check if the current item can be added without exceeding the budget
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)  # Add item to the list
            total_cost += details['cost']  # Update total cost
            total_calories += details['calories']  # Update total calories
    
    return selected_items, total_calories

# Dynamic programming algorithm to maximize total calories within the budget
def dynamic_programming(items, budget):
    # Initialize the DP table
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.keys())  # List of item names
    
    # Fill the DP table
    for i in range(1, len(items) + 1):
        item_name = item_list[i - 1]  # Current item name
        cost = items[item_name]['cost']  # Cost of the current item
        calories = items[item_name]['calories']  # Calories of the current item
        
        for w in range(budget + 1):
            if cost <= w:
                # Update the DP table by considering the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                # If the current item cannot be included, carry forward the previous value
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the selected items
    w = budget
    selected_items = []
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_list[i - 1]
            selected_items.append(item_name)  # Add item to the selected list
            w -= items[item_name]['cost']  # Reduce the budget by the cost of the item
    
    selected_items.reverse()  # Reverse the list to maintain the order
    total_calories = dp[len(items)][budget]  # Total calories is the value in the last cell of the DP table
    
    return selected_items, total_calories

# Test the greedy algorithm
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Selected items (Greedy):", selected_items_greedy)
print("Total calories (Greedy):", total_calories_greedy)

# Test the dynamic programming algorithm
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Selected items (DP):", selected_items_dp)
print("Total calories (DP):", total_calories_dp)
