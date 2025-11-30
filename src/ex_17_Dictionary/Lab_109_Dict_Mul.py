student_info1 = {
    "name" : "Zee Zee",
    "age" : 22,
    "group" : "MBA Marketing",
    "address" : {
        "Home country" : "Madagascar",
        "second country" : "Peru"
    }
}
student_info2 = {
    "name" : "Oo Zee Zee",
    "age" : 24,
    "group" : "Finance",
    "address" : {
        "Home country" : "Germany",
        "second country": "France"
    }
}
student_info3 = {
    "name" : "Be Zee",
    "age" : 20,
    "group" : "Arts",
    "address" : {
        "Home country" : "Poland",
        "second country": "United Kingdom"
    }

}
student_list = [student_info1, student_info2, student_info3]
print(student_list)
print(student_list[2]["group"])
print(student_list[2]["address"]["second country"])