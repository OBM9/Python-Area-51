import time
my_time = int(input("Enter time in seconds: "))

for x in range(0, my_time):
    print(f"Time elapsed: {x + 1} seconds")

time.sleep(3)
print("Time up!")