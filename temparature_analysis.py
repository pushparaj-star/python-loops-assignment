# Name: Pushparaj
# Roll Number: IITP_AIMTN_2602727
# Assignment: Python Loops & Automation - Subjective Question
print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
highest = temperatures[0]
#print(highest)
lowest = temperatures[0]
#print(lowest)
for i in temperatures:
    if (i > highest):
        highest = i
    if (i < lowest):
        lowest = i
print(f"Highest Temparature : {highest}°C")
print (f"Lowest Temparature : {lowest}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count = 0
day = 0

for i in temperatures:
    if (i <= 30):
        continue
    count+= 1
        
print(f"Hot days (>30°C): {count}")

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
day = 0
hot = 0
for i in temperatures:
    day+=1
    if (i>=40):
        break
    if (i>30):
        hot+=1
    
print(f"Hot Days before alert: {hot}")
print(f"Alert! Extreme temperature 40°C detected on Day {day}")