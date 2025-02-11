import json
print(json.__file__)  # Checking the location of the JSON module

# Example 1: Creating a Python dictionary and dumping it into a JSON file
data = {
    "id": 101,
    "name": "Ruchi",
    "salary": 4500000.00,
    "status": False
}
# Dump the Python dictionary into a JSON file
with open("data.json", "w") as file:  # Write into JSON file
    json.dump(data, file, indent=4)

# Example 2: Creating a Python dictionary and dumping it into a JSON file
Employee = {"name": "Ruchitha.Boddu", "ID": "TGTS106", "Role": "Software Engineer"}
with open("Employee.json", "w") as file:
    json.dump(Employee, file, indent=4)

# Example 3: Creating a Python dictionary and converting it into a JSON string
dummy = {"id": 106, "name": "Ruchi", "salary": 5555555.00}
# Convert dictionary to JSON string and print it
json_string = json.dumps(dummy, indent=2)
print(json_string)  # Check JSON format
print("Data Type:", type(json_string))  # Should be <class 'str'>

# Writing JSON string to a file properly
with open("dummy.json", "w") as file:
    file.write(json_string)  # Save JSON string into file