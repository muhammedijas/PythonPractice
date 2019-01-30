#is_instance or issubclass

class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

class devoleper(employee):
    raise_amt=1.10

    def __init__(self,first,last,pay,prgm_language):
        super().__init__(first,last,pay)
        self.prgm_language=prgm_language

class manager(employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ('-->',emp.fullname())

#emp_1=employee('Mthu','Jamshi',1000)
#dev_1=devoleper('Muhammed','Ijas',1000,'Python')
#dev_2=devoleper('Muhammed','Nabeel',1000,'Python')
#dev_3=devoleper('Muhammed','Favas',1000,'Python')

#Mngr_1 =manager('Jasmin','Mytheen',5000,[dev_1])
#Mngr_1.add_employee(dev_2)
#Mngr_1.add_employee(dev_3)
#Mngr_1.add_employee(emp_1)
#Mngr_1.print_emps()

#print(isinstance(Mngr_1,manager))
print(issubclass(employee,devoleper))
