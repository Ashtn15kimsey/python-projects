#parent class
class Organism:
    name = "unknown"
    species = "unknown"
    legs = NONE
    arms = NONE
    dna = "sequence A"
    orgin = "uknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nspecies: {}\nlegs: {}\arms: {}\ndna {}\norigin {}\ncarbon_based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.carbon_based)
        return msg

#child class instance
class Human(organisim):
    name = "mac"
    species = "homosapien"
    legs = 2
    arms = 2
    orgin = "earth"

    def ingenuity(self):
        msg = "\nCreate a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

## another class instanc
class Dog(organisim):
     name = "spots"
     species = "canine"
     legs = 4
     arms = 0
     dna = "sequence B"
     orgin = "earth"

     def bite(self):
         msg = "\nEmits a loud, menacing growl and bites down ferociously on itst target!"
         return msg
#another child class instances
class Bacterium(organisim):
    name = "X"
    species = "Bacteria"
    legs = 0
    aema = 0
    dna = "sequence C"
    orgin = "Mars"


    def replication(self):
        msg = "\nThe cells begin to divide and multpily into two seperate organismims!"
        return msg
    



    
    if __name__ == " __main__":
        human = Human()
            print(human.information())
            print(human.ingenuity())

            dog = Dog()
            print(dog.information())
            print(dog.bite())

            bacteria = bacterium()
            print(bacteria.information())
            print(bacteria.replication())
            
                
    
