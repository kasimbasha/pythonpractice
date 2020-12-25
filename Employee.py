#author : Kasim
class Employee:
    def __init__(self,f,l ):
        self.f = f
        self.l = l
       # self.email = f+'.'+l+'@email.com'
    @property
    def email(self):
        print(f'{self.f}.{self.l}@email.com')
    @property
    def fullname(self):
        print(f' {self.f} {self.l}')
    @fullname.setter
    def fullname(self,name):
        f,l = name.split(' ')
        self.f,self.l = f,l


emp_2 = Employee('Kasim','Basha')
print(emp_2.email)
emp_2.fullname ='Rida Fatima'
print(emp_2.fullname)
print(emp_2.email)

