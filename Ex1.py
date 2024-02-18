percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
calories = int(input())
percent_water = int(input())

total_fat = (calories * (percent_fat / 100)) / 9
total_protein = (calories * (percent_protein / 100)) / 4
total_carbs = (calories * (percent_carbs / 100)) / 4

total_weight = total_fat + total_protein + total_carbs
kcal_per_gram = calories / total_weight

percent_weight = (100 - percent_water) / 100
act_kcal_per_gram = kcal_per_gram * percent_weight
print(f"{act_kcal_per_gram:.4f}")
