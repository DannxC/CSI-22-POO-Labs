class Fish:
    def swim(self):
        return "I can swim!"

class Boat:
    def swim(self):
        return "I can float on water!"

def swim_with_objects(objects):
    for obj in objects:
        print(obj.swim())

fish = Fish()
boat = Boat()

# Lista de objetos com diferentes classes
objects = [fish, boat]

# Ilustrando Duck Typing
swim_with_objects(objects)
