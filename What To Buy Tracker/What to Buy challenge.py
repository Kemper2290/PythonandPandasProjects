# 10,25,5,15
# hammer,saw,nails,brush
# 12



prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below

for  price,item in zip(prices,items):
    if price <= budget_per_item:
        affordable_items.append(item)
        total_needed += price
    elif price >= budget_per_item:
        cant_afford += 1
        continue





print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
