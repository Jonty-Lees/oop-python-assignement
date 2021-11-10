
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


wolf= TalkingDog(breed = "Wolf", speed= "20mph", bark_strength=80, age=40)

wolf.bark()
wolf.dog_years()