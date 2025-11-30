student_info1 = {
    "name" : "Trinad",
    "age" : 22,
    "group" : "Electronics",
    "address" : {
        "city" : "San Jose",
        "state" : "CA",
        "country" : "USA"
    }
}
student_info2 = {
    "name" : "veera",
    "age" : 24,
    "group" : "IT",
    "address" : {
        "city" : "Munich",
        "state" : "Bavaria",
        "country" : "Germany"
    }
}
student_list = [student_info1, student_info2]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["address"]["city"])
print(student_list[0]["address"]["state"])
print(student_list[0]["address"]["country"])
print(student_list[1]["address"]["city"])
print(student_list[1]["address"]["state"])
print(student_list[1]["address"]["country"])