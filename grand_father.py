
class Grand_father:
    def __init__(self,gf_surname,gf_age,gf_citizenship):
        self.name = gf_surname
        self.age = gf_age
        self.citizenship = gf_citizenship

    def properties(self):
        return 'grand father owns a house and has some money'

    def son(self):
        return 'Grand Dad has one son and his name is James'

    def display(self):
        return (f'My grand father name is {self.name},  he is {self.age}, years old and He is  {self.citizenship}')


#
# print(f' {gf1.properties()} and,{gf1.son()}')



