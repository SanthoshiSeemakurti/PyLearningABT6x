student_info = {
    "name" : "Tara",
    "age" : 16,
    "group" : "MPC",
    "address" : "Vizag"
}
print(student_info)
student_info['name'] = "Tara.Venu"
print(student_info["group"])
del student_info["age"]
print(student_info)
print(student_info["name"])
student_info["age"] = 18
print(student_info)