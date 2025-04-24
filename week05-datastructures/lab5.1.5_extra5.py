student = {
    "name":"Mary",
    "modules":[
        {
            "courseName":"Programming",
            "grade":45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}

print("Type Name Modules or Grade to read get the data OR blank string to quit")

user_input = input("Enter option: ")

while user_input != "":
    user_input = input("Enter option: ")
    if user_input == "Name":
        print(student["name"]) 
    elif user_input == "Modules":
        print(student["modules"][0]["courseName"])
        print(student["modules"][1]["courseName"])
    elif user_input == "Grade":
        print(student["modules"][0]["grade"])
        print(student["modules"][1]["grade"])
        
