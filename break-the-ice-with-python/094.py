# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

chicken_details = {"Head":1, "Leg":2}
Rabbit_details = {"Head":1, "Leg":4}

Total_Heads = 35
Total_Legs = 94

chicken = 0
rabbit = 0

# Go from 0 to 35 Chickens
for c in range(36):
    chicken = c
    rabbit = 35-chicken
    if chicken+rabbit == 35:
        # should always be 35
        if chicken*chicken_details["Leg"] + rabbit*Rabbit_details["Leg"] == 94:
            break

print(f'Total Chickens are {chicken} & the Total Rabbits are {rabbit}.')