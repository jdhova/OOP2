
from Father import *

### Multi Level from Grand Father to Father then son

class Son(Father):
    def __init__(self,hobby,gf_surname,gf_age,gf_citizenship,marital_status):
        Father.__init__(self,hobby,gf_surname,gf_age,gf_citizenship)  ### This values are from the father and Must be in same order as above
        self.marital_status = marital_status

    def son_display(self):
        return (f' my Grand Dad name is {self.name} and he is {self.age} years old'
                f' my fathers hobby is {self.hobby} and occupation is {self.occupation()}'
                f' my marital status is {self.marital_status}')

    def kids_display(self, name):
        self.name = name
        return f' my name is {name} I have 2 kids'



# Son1 = Son('Coding','Coleman',76,'Canadian','Married')
# print(Son1.son_display())


### Double level Inheritance from Father and Mother

class Daughter(Father,Mother):
    def __init__(self,hobby,gf_surname,gf_age,gf_citizenship,mom_occupation,mom_citizenship,marital_status):
        Father.__init__(self,hobby,gf_surname,gf_age,gf_citizenship)  ### This values are from the father and Must be in same order as above
        Mother.__init__(self,mom_occupation,mom_citizenship)
        self.marital_status = marital_status

    def daughters_display(self):
        return (f' my Grand Dad name is {self.name} and he is {self.age} years old'
                f' my fathers hobby is {self.hobby} and occupation is {self.occupation()}'
                f'my moms is {self.mom_citizenship} and she is a {self.mom_occupation}'
                f' my marital status is {self.marital_status}')

    def kids_display(self,name):
        self.name = name
        return f' my name is {name} and I have 3 kids'



Daughter1 = Daughter('Coding','Coleman',76,'Canadian','Nurse','American','Married 6 years')
print(Daughter1.daughters_display(),Daughter1.kids_display('Ariel'))


Son1 = Son('Coding','Coleman',76,'Canadian','Married 5 years')
print(Son1.son_display(),Son1.kids_display('Jayden'))


#
# print(father1.display())
# print(father1.son())