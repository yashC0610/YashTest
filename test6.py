## Incapsulation : Changing the Private Variable by invoking Method
## The method is called setter method and we can set the variable by setter
## Incapsulation allows to set the variable using setter method

class ineuron1:

    __student1 = "Data Science"

    def student(self):
        print(self.__student1)

    def student_change(self,new_val):
        self.__student1=new_val

i1 = ineuron1()
i1.student()
i1.__student1="Big Data"
i1.student()
i1.student_change('pritam')
i1.student()

