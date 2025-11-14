class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks >=90:
            print(self.name,"got an A grade!")
        elif self.marks >=75:
            print(self.name,"got a B grade!")
        elif self.marks >=40:
            print(self.name,"got a c grade!")
        else:
            print(self.name,"is failed:(")
s1=student("Ron",98)
s2=student("Harry",80)
s3=student("Luna",52)
s4=student("Voldemort",1)
s1.grade()
s2.grade()
s3.grade()
s4.grade()

    
