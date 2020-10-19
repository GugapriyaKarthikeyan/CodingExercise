#Python class to store the details of the students of a class 
class Students:
    id
    total_marks = 0
    average_marks = 0 
    name_email = {}
    marks = {}

 #Acts as a setter function to set the values to objects   
    def input(self):
        self.id = 1
        self.name_email = {"GugaPriya":"GugaKarthi@gmail.com"}
        self.marks =  {'English':80,'Maths':90,'Science':90}

#This function computes the average marks of a student
    def compute_average(self):   
        mark_list = self.marks.values();
        self.total_marks = 0
        for i in mark_list:
            self.total_marks = self.total_marks+i
        
#This function displays all the details of a particular student        
    def display(self):  
        print("Student Id : ", self.id) 
        print("Student name :", self.name_email.keys())
        print("Student Email ID :",self.name_email.values())
        print("Student Average Marks :",self.total_marks/3)

Guga = Students()
print("Student Details:") 
Guga.input()
Guga.compute_average()
Guga.display()


