
score = 10
high_score = 200
low_score = 3

score_list = [score, high_score, low_score]
print(f"original list: {score_list}")

score_list.append(150)
print("sorted list: {}".format(sorted(score_list)))

student_names = ['Anna', 'Belle', 'Carter']
new_student = input("Welcome, student! Whats your name")
student_name.append(new_student)

chocolates = {
'white': 1.50,
'milk': 1.20,''
'dark': 1.80,
'vegan': 2.00,
}


user_flavour = input("Which chocolate flavour do you want? We have white, milk, dark and vegan ")
user_qty = input("Sure, how many do you want  ")
qty = int(user_qty)
print("The total will be: ", qty*chocolates[user_flavour])

