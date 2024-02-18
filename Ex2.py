import math

days = int(input())
food_left = int(input())
food_per_day_1 = float(input())
food_per_day_2 = float(input())
food_per_day_3 = float(input())

total_food_needed = (days * (food_per_day_1 + food_per_day_2 + food_per_day_3))

if total_food_needed <= food_left:
    food_left = math.floor(food_left - total_food_needed)
    print(f"{food_left} kilos of food left.")
else:
    food_needed = math.ceil(total_food_needed - food_left)
    print(f"{food_needed} more kilos of food are needed.")
