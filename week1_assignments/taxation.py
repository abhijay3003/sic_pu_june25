Employee_name = input("Enter the  employee Name : ")
Employee_id = int(input("Enter the employee id :"))
Basic_Monthly_salary = int(input(" Enter the employee basic monthly salary: "))
Special_Allowances = int(input(" Enter the account of Special Allowances : "))
Bouns_percentage = int(input("Enter the bouns withou % symbol : "))
Bouns_amount = (Bouns_percentage/100) * Basic_Monthly_salary
Gross_monthly_salary = Basic_Monthly_salary + Special_Allowances
Annual_gross_salary = (Gross_monthly_salary * 12) +Bouns_amount
print("employee name: {}\nemployee id: {}\ngross monthly salary: {}\nannual gross salary: {}".format(Employee_name, Employee_id, Gross_monthly_salary, Annual_gross_salary))
Standard_deduction = 50000
Taxable_income = Annual_gross_salary - Standard_deduction
print('Standard deduction : {}\ntaxable income : {}'.format(Standard_deduction,Taxable_income))
