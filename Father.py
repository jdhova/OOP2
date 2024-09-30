from grand_father import *
### Single  Level from Grand Father to Father then son
class Father(Grand_father):
    def __init__(self,hobby,gf_surname,gf_age,gf_citizenship):
        super().__init__(gf_surname,gf_age,gf_citizenship)
        # Grand_father.__init__(self,gf_surname, gf_age, gf_citizenship)
        self.hobby = hobby

    def occupation(self):
        return ('Data Scientist ')

    def display(self):
        return (f'Grand dad surname is {self.name} he is {self.age} years old and he is {self.citizenship}, while my fathers hobby is {self.hobby}')



class Mother:
    def __init__(self,mom_occupation,mom_citizenship):
        self.mom_occupation = mom_occupation
        self.mom_citizenship = mom_citizenship

    def display(self):
        return (f'Mom is {self.mom_occupation} and she is from {self.mom_citizenship}')



