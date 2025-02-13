import json
print(json.__file__)  # Checking the location of the JSON module

# Example 1: Creating a Python dictionary and dumping it into a JSON file
data = {
    "id": 101,
    "name": "Ruchi",
    "salary": 4500000,
}
with open("my_data.json", "w") as file:  #  Open file named(my_data.json) to Write JSON data
    json.dump(data, file, indent=4)   # Convert dictionary to JSON and write to file as text
with open("my_data.json","r") as file:
    idata=json.load(file) #de-serialization
    print("Ex1=Data Type:",type(idata),) # Should print <class 'dict'>
    print("JSON file to Python Object:",idata)

# Example 2: Creating a Python dictionary and dumping it into a JSON file
Employee = {"name": "Ruchitha.Boddu", "ID": "TGTS106", "Role": "Software Engineer"} # Creating the dictionary
with open("Member.json", "w") as file:  # open file named(Member.json) to write JSON data
    json.dump(Employee, file, indent=4)  # Convert python dictionary to JSON and write to file
with open("Member.json", "r") as file:  # Read JSON from a file and convert to Python object
     pfile=json.load(file) ## Convert JSON to dictionary, de-serialization
     print("Ex2=Data Type:", type(pfile))  # Should print <Class 'dict'>
     print("JSON file to python Object:",pfile)

# Example 3: Creating a Python dictionary and converting it into a JSON string
dummy = {"id": 106, "name": "Ruchi", "salary": 5555555}
json_string = json.dumps(dummy, indent=2) # Convert dictionary to JSON string
print(json_string)  # Check JSON format
print("Ex3=Data Type:", type(json_string))  # Should be <class 'str'> only for READ
with open("dummy.json","r") as file:
    dfile=json.loads(json_string) # de-serialization
    print("JSON String to Python Object:",dfile)




