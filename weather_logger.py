temps = []

while True:
    value = input("Enter temperature ('done' to stop): ")

    if value == "done":
        break

    temps.append(float(value))

def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }

print(summarize(temps))