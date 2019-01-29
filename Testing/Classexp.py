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

    @classmethod
    def set_inc_constant(cls,amt):
        cls.amt=amt

    @classmethod
    def format_string(cls,inpt):
        first,last,pay=inpt.split('-')
        return cls(first,last,pay)


#e1=employee('muhammed','ijas',1000)
#e2=employee('muhammed','nabeel',2000)
#e3=employee('muhammed','favas',3000)

emp_str = 'Muthu-shingles-2000'
e4=employee.format_string(emp_str)

#below comment is equal to  employee.amt=1.8

#employee.set_inc_constant(1.8)
print(e4.fullname())

#print(employee.amt)
#print(e1.amt)
#print(e2.amt)
#print(e1.increment())
#print(e2.increment())

