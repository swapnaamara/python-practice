#variables with the same name 
name1 = "john"
name2 = "john"

#check if name1 and name2 refer to diff objects in memory
result_is_not = name1 is not name2
print("name1 is not name2?",result_is_not)


num1 = 10
num2 = 20
result_is = num1 is not num2
print("num1 is not num2?",result_is)
