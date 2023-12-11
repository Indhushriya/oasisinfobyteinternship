from termcolor import colored
print("\033[1;37;40m+-----------------------------------------------+")
print("     |           \033[1;34;40mBMI Calculator\033[1;37;40m          |       ")
print("+-----------------------------------------------+\033[0m\n")

height=float(input("Height in m : "))
weight=float(input("Weight in kg : "))
print("\n+-------------------------------------+")
result=weight/height**2
bmi = round(result,2)


print(colored("             BMI:", 'cyan'), colored(f"{bmi:.2f}", 'yellow'), colored("", 'cyan'))
print("+-------------------------------------+\n")
if result<18.5:
    print("Category : Underweight")
    print("Fuel up and build strength for a healthier you!🍴\n")
elif result>=18.5 and result<25:
    print("Category : Normal")
    print("Keep up the good work, you're on the right track!🤗\n")
elif result>=25 and result<30:
    print("Category : Overweight")
    print("Let's focus on healthy habits to reach your best self!🚴\n")
else:
    print("Category : Obese")
    print("Small changes can lead to big results. You've got this!🏃🏽\n")
