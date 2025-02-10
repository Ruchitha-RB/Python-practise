import json
print(json.__file__)
# Create a Python dictionary file
data = {
    "id": 101,
    "name": "Ruchi",
    "salary": 4500000.00,
    "status": False
}
# Dump the dictionary into a JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # `indent=4` makes it more readable

#CReate a string python dictionary
Employee ={"name":"Ruchitha","ID":"TGTS106","Role":"Software Engineer"}
#Dump the dictionary into json string
with open("Employee.json","w") as file:
    json.dump(Employee,file,indent=1)

    data = {"id": 106, "name": "Ruchi", "salary": 5555555.00, "status": True}

    json_string = json.dumps(data,indent=2)  # Convert to JSON string
    print(json_string)  # Check JSON format

    # Verify the type
    print("Data Type:", type(json_string))  # Should print: <class 'str'








