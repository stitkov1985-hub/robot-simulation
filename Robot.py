# Начальные данные
x = 0
y = 0

print("Hello! I'm a robot. Teams: w (up), s (back), a (left), d (right), exit")

while True:
    print(f"My coordinates: x={x}, y={y}")
    team = input("Where to go? ").lower()

    if team == "d":
        y += 1
    elif team == "a":
        y -= 1
    elif team == "s":
        x -= 1
    elif team == "w":
        x += 1
    elif team == "exit":
        print("Bye!")
        break
    else:
        print("I don't know such a command..")
