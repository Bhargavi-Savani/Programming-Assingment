class emp:

    def message(self):
        print('This message is from Employee Class.')


class Dept(emp):

    def message(self):
        print('This Department class is inherited from Employee.')


Emp = emp()
Emp.message()

dept = Dept()
dept.message()
