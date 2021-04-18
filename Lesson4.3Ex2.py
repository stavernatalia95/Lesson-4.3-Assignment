employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]

def replace_employee(employee_shift,old_employee,new_employee):
    index = employee_shift.index(old_employee)
    employee_shift[index] = new_employee

print("Before function call")
print(employee_shift)

replace_employee(employee_shift,"Kelly","Maria")

print("After function call")
print(employee_shift)
