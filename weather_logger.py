temps = []

while True:
    value = input("Enter temperature ('done' to stop): ")

    if value == "done":
        break

    temps.append(float(value))

print(temps)