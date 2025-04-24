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

print("student: {}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))