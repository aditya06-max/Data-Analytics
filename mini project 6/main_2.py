arr = [5, 10, 50, 56, 84, 27, 100]

# Assume the first day's price is the minimum price
min_price = arr[0]

# Initially, profit is 0
max_profit = 0

# Start checking from the second day
for price in arr[1:]:

    # Calculate profit if we sell today
    profit = price - min_price

    # Update maximum profit if today's profit is greater
    if profit > max_profit:
        max_profit = profit

    # Update the minimum buying price if today's price is lower
    if price < min_price:
        min_price = price

print("Maximum Profit:", max_profit)