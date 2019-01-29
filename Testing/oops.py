class employee:

    num_of_emp = 0
    amt = 1.1

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

        employee.num_of_emp += 1

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))


    def increment(self):
        self.pay=int(self.pay * self.amt)
        return self.pay



e1=employee('muhammed','ijas',1000)
e2=employee('muhammed','nabeel',2000)
e3=employee('muhammed','favas',3000)

print(e1.pay)
print(e1.increment())
e1.amt=1.5
print(e1.increment())
print(e1.pay)


