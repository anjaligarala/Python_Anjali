class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog name is {self.name} and age for Dog is {self.age}"

    def speak(self, sound):
        return f"{self.name} says {sound}"


anjali = Dog('Anjali', 28, )
sohil = Dog('Sohil', 30)
sound = "Bow Wow"

print(anjali)
print(anjali.speak(sound))
