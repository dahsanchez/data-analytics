name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print(name_1.title())
print(name_2.title())
print(name_3.title())

print(salary_1.replace('$',''))
print(salary_2.replace('$',''))

int_salary = int(salary_1.replace('$', '').replace(',',''))
print(int_salary)
print(type(int_salary))