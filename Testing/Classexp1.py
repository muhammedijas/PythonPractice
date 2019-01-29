# static class, it wont have instance or cls

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

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        return True

import datetime
my_date=datetime.date(2017,5,18)
print (my_date)
print(employee.is_workday(my_date))