class Animal: 
 
    def __init__(self, species, sound):
        self.species = species
        self.age =  0
        self.sound = sound 

    def toString(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment):
        if self.age + increment < 4:
            self.age = increment + self.age

            if self.age > 4 :
                self.age = 4
        else: 
            print(f"warning: {self.species} morreu")
            self.age = 4


    def makeSound(self):
        if self.age == 0 :
            return "---"
              
        elif self.age == 4:
            return "RIP"


            
        return f"{self.sound}"




def main():
    animal = Animal("", "")
    while True:
        line: str = input()
        print(f"${line}", end="\n")
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "grow":
            animal.ageBy(int(args[1]))

        elif args[0] == "noise":
            print(animal.makeSound())


        elif args[0] == "show":  
            print(animal.toString())

main()

    


      
        


