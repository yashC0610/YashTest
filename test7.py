## Polymorphism : .

class ineuron:

    def student(self):
        print('student details: ')

class class_type:

    def student(self):
        print("print the class type of student")

## Function is behaving like bridge or connection betwenn all the classes
## Function behave differently as per different object


i=ineuron()
j=class_type()

def ineuron_external(a): ## external function
    a.student()

ineuron_external(i)
ineuron_external(j)




