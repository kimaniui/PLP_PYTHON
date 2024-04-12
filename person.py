class Person:
            def __init__(self, name, age, gender):
                self.name = name
                self.age = age
                self.gender = gender

        def introduce(self):
                print(f'Hello, my name is {self.name} and I am a {self.gender} of {self.age} years old')

std = Person('John', 20, 'male') 