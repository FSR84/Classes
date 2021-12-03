from dataclasses import dataclass



# regular class 
class Person:

    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print('Regular Class results:')

print(id(person1))
print(id(person2))

print(person1) # will give error

print(person2 == person3) # will compare objects, not their properties



# data class
@dataclass
class PersonD:
    name: str
    job: str
    age: int    


person1 = PersonD("Geralt", "Witcher", 30)
person2 = PersonD("Yennefer", "Sorceress", 25)
person3 = PersonD("Yennefer", "Sorceress", 25)

print('Data Class results:')

print(id(person1))
print(id(person2))

print(person1) # will print "PersonD(name='Geralt', job='Witcher', age=30)"

print(person2 == person3) # will compare the properties of objects

