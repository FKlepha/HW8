class Person:
    def __init__(self, name, lastname, age):
        self.__name = name
        self.__lasname = lastname
        self.__age = age

    def say_hello(self):
        print(f'Hello my name is {self.__name} im {self.__age} old')

    def info(self):
        print(f'name = {self.__name}, age = {self.__age}, lastname = {self.__lasname}')

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_age(self, age):
        if isinstance(age, str):
            try:
                age = int(age)
            except Exception:
                age = 2
        if age > 0 and age < 100:
            self.__name = age
        else:
            self.__age = 0


person = Person('Ivan', 'Ivanov', 25)
person1 = Person('Petr', 'Ivanov', 25)
person1 = Person('Petr', 'Ivanov', 16)
person1 = Person('Petr', 'Ivanov', 30)
person1 = Person('Petr', 'Ivanov', 5)

print(person)
person.info()
person.say_hello()
person1.say_hello()

def older(li, age):
    li1 = []
    for p in li:
        if p.get_age() > age:
            li1.append(p)
    return li1


person = Person('Ivan', 'Ivanov', 25)
person1 = Person('Petr', 'Ivanov', 25)
person1 = Person('Petr', 'Ivanov', 16)
person1 = Person('Petr', 'Ivanov', 30)
person1 = Person('Petr', 'Ivanov', 5)
print(*li1)


#self - обращение к текущему объекту
#принципы ООП:
# 1. Инкапсюляция - сокрытие реализации, применяется для написании безопасного кода