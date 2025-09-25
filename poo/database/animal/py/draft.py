class Animal: 
 
    def __init__(self, species, sound):
        self.species = species
        self.age =  0
        self.sound = sound 

    def toString(self):
        return "f{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment):
        if self.age < 4 :
            self.age =+ increment

            if self.age > 4 :
                self.age = 4
        else: 
            print(f"warning: {self.species} morreu")


    def makeSound(self):
        if self.age == 0 :
            return "---"
              
        elif self.age == 4:
            return "RIP"


            
        return "f{self.sound}"

      
        


