print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
minimum = temperatures[0]
maximum = temperatures[0]
for i in temperatures:
    if (i>=maximum):
        maximum=i
    if (i<=minimum):
        minimum=i

print(f"Highest Temperature: {maximum}°C")
print(f"Lowest Temperature: {minimum}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot = 0
for i in temperatures:
    if (i==30):
        continue
    if (i>30):
        hot+=1
print(f"Hot Days (>30°C): {hot}")

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

day = 0
hot = 0

for i in temperatures:
    day += 1
    if (i>=40):
        break
    if (i>30):
        hot +=1

print (f"Hot Days before alert: {hot}")
print (f"Alert! Extreme temperature 40°C detected on Day {day}")