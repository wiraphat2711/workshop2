class Person:
    def __init__(self, nume, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_into(self):
        return {"name": self.name, "age": self.age}


name = "pipusana petgumpoom"
age = 26
address = "London"

person = Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_into())