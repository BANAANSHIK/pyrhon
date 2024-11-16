class person:
    name = ' никто '
    weight = 0
    height = 0
    def __init__(self, newName, newHeight, newWeight):
        self.height = newHeight
        self.name = newName
        self.weight = newWeight

    def walk(self):
        print(self.name, 'гулянькает')
        
    def talk(self):
        print(self.name, 'разговваривает с петей')

    
class dog:
    nickname = ' никто '
    doing = ''

    def __init__(self, newNickname, newDoing):
        self.Nickname = newNickname
        self.Doing = newDoing


    


person_1 = person('порося', 220, 500)
person_2 = person('gg', 1, 100000)

person_1.walk()
person_2.walk()

person_1.talk()
person_2.talk()

dog_1 = dog('lol', 'jump')
dog_2 = dog('lal', 'poop')

