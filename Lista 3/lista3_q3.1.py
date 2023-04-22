from abc import ABC, abstractmethod

# o uso do módulo abc (Abstract Base Class) e o 
# decorador abstractmethod ajudam a definir e reforçar 
# a natureza abstrata da classe.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Au au!"

class Cat(Animal):
    def speak(self):
        return "Miau!"

class Bird(Animal):
    def speak(self):
        return "Piu piu!"

def speak_with_animals(animals):
    for animal in animals:
        print(animal.speak())

# Lista de animais com diferentes subclasses
animals = [Dog(), Cat(), Bird()]

# Ilustrando polimorfismo
speak_with_animals(animals)