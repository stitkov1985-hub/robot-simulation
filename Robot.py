# Начальные данные
x = 0
y = 0

print("Hello! I'm a robot. Teams: w (up), s (back), a (left), d (right), exit")

while True:
    print(f"My coordinates: x={x}, y={y}")
    команда = input("Where to go? ").lower()

    if команда == "d":
        y += 1
    elif команда == "a":
        y -= 1
    elif команда == "s":
        x -= 1
    elif команда == "w":
        x += 1
    elif команда == "exit":
        print("Bye!")
        break
    else:
        print("I don't know such a command..")
