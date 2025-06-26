Employee_name = input("Enter the  employee Name : ")
Employee_id = int(input("Enter the employee id :"))
Basic_Monthly_salary = int(input(" Enter the employee basic monthly salary: "))
Special_Allowances = int(input(" Enter the account of Special Allowances : "))
Bouns_percentage = int(input("Enter the bouns withou % symbol : "))
Bouns_amount = (Bouns_percentage/100) * Basic_Monthly_salary
Gross_monthly_salary = Basic_Monthly_salary + Special_Allowances
Annual_gross_salary = (Gross_monthly_salary * 12) +Bouns_amount
print("employee name: {}\nemployee id: {}\ngross monthly salary: {}\nannual gross salary: {}".format(Employee_name, Employee_id, Gross_monthly_salary, Annual_gross_salary))
# level 2
Standard_deduction = 50000
Taxable_income = Annual_gross_salary - Standard_deduction
print('Standard deduction : {}\ntaxable income : {}'.format(Standard_deduction,Taxable_income))
# level 3
Tax = 0
if Taxable_income <= 300000:
    Tax = 0
elif Taxable_income <= 600000:
    Tax = (Taxable_income - 300000) * 0.05
elif Taxable_income <= 900000:
    Tax = (300000 * 0.05) + (Taxable_income - 600000) * 0.10
elif Taxable_income <= 1200000:
    Tax = (300000 * 0.05) + (300000 * 0.10) + (Taxable_income - 900000) * 0.15
elif Taxable_income <= 1500000:
    Tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (Taxable_income - 1200000) * 0.20
else:
    Tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (Taxable_income - 1500000) * 0.30
if Taxable_income <= 700000:
    rebate = min(Tax, 25000)
    Tax -= rebate
else:
    rebate = 0
if Tax > 0:
    cess = Tax * 0.04
else:
    cess = 0
Total_tax_payable = Tax + cess
# level 4
Net_salary = Annual_gross_salary - Total_tax_payable
print("Annual Gross Salary : {}\nTotal Tax Payable : {}\nAnnual Net Salary : {} ".format(Annual_gross_salary,Total_tax_payable,Net_salary))
# level 5
print("="*50)
print("           Employee Tax Computation Report")
print("="*50)
print("Employee Name        : {}".format(Employee_name))
print("Employee ID          : {}".format(Employee_id))
print("-" * 50)
print("Gross Monthly Salary : {:,.2f}".format(Gross_monthly_salary))
print("Annual Gross Salary  : {:,.2f}".format(Annual_gross_salary))
print("-" * 50)
print("Standard Deduction   : {:,.2f}".format(Standard_deduction))
print("Taxable Income       : {:,.2f}".format(Taxable_income))
print("-" * 50)
print("Tax Breakdown:")
if rebate > 0:
    print("  Tax before Rebate  : {:,.2f}".format(Tax + rebate))
    print("  87A Rebate         : {:,.2f}".format(rebate))
else:
    print("  Tax                : {:,.2f}".format(Tax))
print("  Cess (4%)          : {:,.2f}".format(cess))
print("Total Tax Payable    : {:,.2f}".format(Total_tax_payable))
print("-" * 50)
print("Net Annual Salary    : {:,.2f}".format(Net_salary))
print("="*50)


