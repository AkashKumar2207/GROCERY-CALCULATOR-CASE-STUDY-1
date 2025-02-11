## Grocery Store Calculator
items = []
prices = []
num_items = int(input("Enter the number of items: "))

for i in range(num_items):
  item_name = input(f"Enter the name of item {i+1}: ")
  item_quantity = int(input(f"Enter the quantity of {item_name}: "))
  item_price = float(input(f"Enter the price of {item_name}: "))

  total_price = item_quantity * item_price
  print(f"The total price of {item_quantity} {item_name} is {total_price:.2f}")
  items.append(item_name)
  prices.append(total_price)

total_cost = sum(prices)
print(f"The total cost of all items is {total_cost:.2f}")



