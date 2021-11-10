
class Dog():

    
    def __init__(self, breed, speed, bark_strength, age):
        self.breed = breed
        self.speed = speed
        self.bark_strength = bark_strength
        self.age = age


    def bark(self):
        if self.bark_strength > 50:
            print("WOOOOOF WOOOOOF")
        else:
            print('woof woof')


    def dog_years(self):
        if self.age:
            dog_age = self.age * 7
            print (f'your dog is {dog_age} in dog years')  
        else: 
            print('Your dog has no age?!')
    
    def species():
        print("Canis lupus familiarise")
    


husky = Dog(breed = "Husky", speed= "20mph", bark_strength=80, age=4)
greyhound = Dog(breed = "Greyhound", speed= "50mph", bark_strength=20, age= 10)


class TalkingDog(Dog):
    def __init__(self, breed, speed, bark_strength, age):
        super().__init__(breed, speed, bark_strength, age)

    def bark(self):
        if self.bark_strength > 50:
            print("HELLLLO")
        else:
            print('hello')

# ASSIGNMENT ADDITIONS

    def __str__(self):
        return f'Breed:{self.breed}\nSpeed:{self.speed}mph\nBark Strength: {self.bark_strength}/100 \nAge:{self.age}'

    def __add__(self, other):
        combined_speed = self.speed + other.speed
        combined_bark_strenght= self.bark_strength + other.bark_strength
        combined_breed = self.breed + other.breed
        return f'Deadly Speed:{combined_speed},\nDeadly Bark:{combined_bark_strenght}/100\nGood Luck trying to escape the {combined_breed} '

wolf= TalkingDog(breed = "Wolf", speed= 85, bark_strength=80, age=6)
poodle= TalkingDog(breed = "Poodle", speed= 3, bark_strength=100, age=2)


print(wolf)

superDog = wolf + poodle

print(superDog)

# ANSWERS:

# - What is the difference between __len__() and len()  in python?

    #  __len__() is customizable in calling the length
    # len() calls and returns the length without any customization

# - What is the purpose of __init__?
    # __init__ is a function that assigns values to object properties when the object is being created