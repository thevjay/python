def infinite_chai():
    count = 1
    while True:
        yield f"Chai cup {count} served"
        count += 1

stall = infinite_chai()
user2 = infinite_chai()

for _ in range(5):  # Limiting to 5 cups for demonstration
    print(next(stall))

for _ in range(3):  # Limiting to 3 cups for demonstration
    print(next(user2))