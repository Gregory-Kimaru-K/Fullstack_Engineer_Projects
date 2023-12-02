lst = [1, 2, 3,4, 5]

print(type(lst))

class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

ft = Dog(breed = "German", age = 10)

print(ft.age)
print(ft.breed)
print(type(ft))