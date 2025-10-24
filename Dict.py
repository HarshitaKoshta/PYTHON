# info = {
#     "key" : "value",
#     "name" : "Pihu",
#     "subj" : ["python","java","html"],
#     "age" : 20 ,
#      2 : 75
# }
# info["name"] = "Harshita"
# info["surname"] = "Koshta"
# print(info)
# print(info["name"])
# print(info["subj"])
# print(info["age"])


student = {
    "name" : "rahul",
    "subj" : {
        "english" : 78,
        "maths" : 97,
        "chemistry" : 84
    }
}
# print(student["subj"]["maths"])

# print(list(student.keys()))
# print(student.values())
# print(student.items())


student.update({"name":"pihu","city":"jabalpur","age":20})
print(student)
