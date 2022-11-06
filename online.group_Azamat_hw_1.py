class Person:
    def __init__(self, the_fullname, the_age, the_is_married):
        self.fullname = the_fullname
        self.age = the_age
        self.is_married = the_is_married


    def introduce_myself(self, fullname, age, is_married):
        print(f'Hi, my name is {fullname}, I am {age} years old and I am {is_married}.'
              f'I have following subjects with grades:')


class Student(Person):
    def __init__(self, the_fullname, the_age, the_is_married):
        super().__init__(the_fullname, the_age, the_is_married)


class Teacher(Person):
    def __init__(self, the_fullname, the_age, the_is_married, salary, exp, base_exp):
        super().__init__(the_fullname, the_age, the_is_married)
        self.salary = salary
        self.exp = exp
        self.base_exp = base_exp


    def wage_calc(self, fullname, salary, base_exp, exp):
        print(f'Teacher {fullname} has annual wage is {salary} US dollars and '
              f'expirience is {exp} years, where base expirience is {base_exp} years.')
        if exp > self.base_exp:
            print(f'As teacher {fullname} has expirience more than 3 years, his annual wage is {salary*0.5+salary} US dollars.')


dict_marks = {'Programming': 5, 'Mathematic': 3, 'Python': 4}
print()
person = Person('fullname', 'age', 'is_married')
person.introduce_myself('Tima', 25, 'single')
for key, value in dict_marks.items():
    print(key, ':', value)
list_values={5,3,4.3}
average=sum(list_values)/len(list_values)
print("The middle average of grades list_values is equal: ",average)
print()

teacher = Teacher('Alex', 100, 3 ,3, 3 ,3)
teacher.wage_calc('Alex', 100, 3, 4)
print()

print('Programming course "Python" has following students:')
dict_student_list = {1: 'John Snow', 2: 'Fredy Cruger', 3: 'Mel Gibson'}
person = Person('fullname', 'age', 'is_married')
for key, value in dict_student_list.items():
    print(key, value)

dict_marks = {'Programming': 3, 'Mathematic': 4, 'Python': 5}
print()
person = Person('fullname', 'age', 'is_married')
person.introduce_myself('John Snow', 18, 'married')
for key, value in dict_marks.items():
    print(key, ':', value)
list_values={3,4,5}
average=sum(list_values)/len(list_values)
print("The middle average of grades list_values is equal:", average)

dict_marks = {'Programming': 3, 'Mathematic': 4, 'Python': 5}
print()
person = Person('fullname', 'age', 'is_married')
person.introduce_myself('Fredy Cruger', 35, 'divorced')
for key, value in dict_marks.items():
    print(key, ':', value)
list_values={5,2,3}
average=sum(list_values)/len(list_values)
print("The middle average of grades list_values is equal:", average)

dict_marks = {'Programming': 3, 'Mathematic': 3, 'Python': 4}
print()
person = Person('fullname', 'age', 'is_married')
person.introduce_myself('Mel Gibson', 25, 'single')
for key, value in dict_marks.items():
    print(key, ':', value)
list_values={3,3,4}
average=sum(list_values)/len(list_values)
print("The middle average of grades list_values is equal:", average)