fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# range(start, stop, step) → custom step

for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in range(1, 6):
    if i == 3:
        continue 
    if i == 5:
        break   
    print(i)
