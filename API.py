import json
print(json.__file__)#checking the locaton of the file
# Create a Python dictionary file
data = {
    "id": 101,
    "name": "Ruchi",
    "salary": 4500000.00,
    "status": False
}
# Dump the python dictionary into a JSON file
with open("data.json", "w") as file:#write into JSON file
    json.dump(data, file, indent=4)

#Creating python dictionary and then dump into a JSON file
Employee ={"name":"Ruchitha.Boddu","ID":"TGTS106","Role":"Software Engineer"}
with open("Employee.json","w") as file:
    json.dump(Employee,file,indent=1)


#Creating python dictionary, and then dump into a  JSON String
    data = {"id": 106, "name": "Ruchi", "salary": 5555555.00}
    json_string = json.dumps(data,indent=2)  # Convert to JSON string
    print(json_string)  # Check JSON format
    print("Data Type:", type(json_string))
    
    
#Read JSON DATA from a file
    with open("Employee.json","r") as file:
     








