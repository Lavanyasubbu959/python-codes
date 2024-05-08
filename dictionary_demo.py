empty_dict = {}
print("emoty_dict : ",empty_dict, type(empty_dict))

employee = {"ename": "Lavanya", "age": 23, "email": "lavanyasubbu959@gmail.com" ,
            "city": "Nashik", "dept": "training", "salary": 5000, "company": "Itvedant"}
print(employee)

print("name : ", employee["ename"], "email : ", employee["email"])
print("city : ", employee.get("city"), "dept : ", employee.get("dept"))


#adding elements to dictionary one at a time
student = {}
print("student : ",student)
student[1] = "Peter"
student[2] = "Ralph"
student[3] = "Ricky"
student[4] = "Joseph"

print("Student dictionary : ", student)

#updating an element of dictionary
name = "Vicky"
student[3] = name
print("student : ",student)