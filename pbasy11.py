
import json
try:
    with open("records.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []
record = {
    "id": int(input("Enter ID: ")),
    "name": input("Enter name: "),
    "age": int(input("Enter age: "))
}
data.append(record)
filename = input("Save to (records.json or new.json): ")
with open(filename, "w") as f:
    json.dump(data, f, indent=4)
print("Record added and saved successfully!")
