# Coding Exercise
## Task 1. What is Linux? Explain 5 linux commands

Linux is an open source Operating System on which a diverse variety of applications and devices are built and it has various distributions and it is written C and Assembly Language. Eg: Mobile devices, Super Computers, Server Computers, Automobiles, Home Appliances, Embedded devices, Cloud Computing, Mainframe computers etc,..

Some examples of Linux Commands are:

* **uname -a** - Provides a wide range of basic information about the system
* **ls** - lists all files and folders in your current working directory.
* **cd** - used to change the current working directory
* **sudo** - allows you to run programs or other commands with administrative privileges, just like “Run as administrator” in Windows
* **apt-get** - used to install, update, upgrade and remove any package

---

## Task 2. Define Linux Kernel?

* Linux kernel is the software forming the core part of Linux Operating system and its modular and highly configurable.
* For a general purpose computer which is capable of running multiple processes simultaneously in the same machine, the kernel virtualizes the common hardware resources of the computer to provide each process with its own virtual resources which is termed as pre-process hardware virtualization.
* The sub-components of Linux kernel are:
    * **Process Scheduler**: It is responsible for fairly distributing the CPU time among all the processes running on the system simultaneously by Process pre-emption and by using process scheduling algorithms. 
    * **Memory Management Unit**: This unit takes care of the physical and virtual memory management by various paging and page replacement policies. 
    * **Virtual and concrete File Systems**: Virtual filesystem is an abstract layer on top of a more concrete file system. The purpose of a VFS is to allow client applications to access different types of concrete file systems in a uniform way and it is used to access local and network storage devices.
    * **Networking sub-system**: It is networking interface facilitating client server connectivity
    * **Inter-process Communication Unit**: It manages the shared data of the processes thereby facilitating inter process communication using Socket, Pipes and Queues. 
    * **Device drivers**: It is the software code part of kernel that forms an interface that supports the communication and ensures the functioning of hardware peripheral devices.

---

## Task 3. What is the difference between 32bit and 64bit computers? How much maximum memory access they can have?

* We refer a computer as 64-bit or 32-bit based on the operation system software that computer uses. The OS software to be installed for a machine depends on two things(processor and RAM), registers in the CPU must be able to store the maximum byte address capacity of the RAM. 
* A 64 bit processor will take the address stored in 64-bit register inside the CPU and use a 64-bit address bus to access the 8 GB RAM which is capable of storing (2 power 64) byte addressable memory locations, where as a 32bit processor won’t be able to completely utilize an 8GB RAM so uses a 4GB RAM for complete utilization of 2 power 32 byte addressable memory locations in the RAM. 
* A 64 bit processor can run smoothly with 4GB RAM but the RAM is too small for such a fast processor. 
* So we choose the OS accordingly in synchronization with processor, RAM size since it has to deal with machine instruction codes for register, peripherals like data and control buses capacity and so on. 
* Application software designed for a 64-bit operating system will never be compatible with 32-bit OS. Since the software uses 64-bit machine instruction codes, clash will arise in hardware capacity to run the 64-bit compatible machine code. But some of the 32-bit application software will run on 64-bit OS not all.

---

## Task 4. What isgit and what version is installed in your Linux machine?

Git is a distributed version control systemwhich maintains different versions of your project when we work in a team or as an individual. As the project progresses, new features get added to it. Since it is a distributed version, it has a local repository of the project in his/her local machine unlike central where team members should have an internet connection to update their work every time to main central repository and the git version installed in my machine is 2.7.4.

---

## Task 5. Create a github account and make a repository.

https://github.com/GugapriyaKarthikeyan/CodingExercise

---

## Task 6. What is low level language and high level language? Give examples.

Two types of programming languages are low level languages and high level languages.

* Low level programming languages are often cryptic and not human-readable but easily recognized and processed by machine. Eg: Assembly Language and Machine Language.
* High level programming language used by the developer to code the software product is easily understood by humans but not by machine, so it must be compiled into a low level machine code by the compiler. Eg: C, C++, Java, etc,...

---

## Task 7. Define objects in the context of object oriented programming. Give code example in any object oriented language.

Object is a real world entity with state, behavior and identity. 

In detail, Any logical and complex system on earth that requires massive computation, problem solving and decision making can be mathematically modeled and can be converted into computer solvable problem by making use of various programming languages to define the algorithmic steps to solve that problem with that language specific syntax rules and stuff - which we call as a software code. 

Of all these programming languages Object-oriented programming is an approach where each real world entity can be modeled as an object in that computer solution to that problem. 

For Eg: Consider a Student Database management system developed as a software application and it is maintained digitally in an educational institution. Then each student in that application is an object with state, behavior and identity. 

**Java code example**

```java
    class Student {
        private int studentId;
        private String studentName;

        public Student(int studentId, String studentName) {
            this.studentId = studentId;
            this.studentName = studentName;
        }

        public static void main(String args[]) {
            Student student = new Student("1","Gugapriya");
        }
    }

```

---

## Task 8. Write a python code to print your linux distribution name and kernel version.

```python
import platform 
print('Python Code displaying the linux distribution name and kernel version')
print
print
print('Distribution : ', platform.linux_distribution())
print('Version : ', platform.version())

#I have installed VMware in my windows system to configure the virtual machine #with Ubuntu Version 16.04 and Python version 3.5.2  

```
---

## Task 9. Write a python code using function, file input and print each line with linenumber in the terminal.

```python
# Python program to print the content of each line of the input file along with line number   
  
List = ["Python is an interpreted, high-level and general-purpose programming language.\n",
     "Its language constructs and object-oriented approach aim to help programmers write clear, logical code.\n",
     "Python is dynamically typed and garbage-collected.\n"] 
  
# Writing to a file 
file = open('AboutPython.txt', 'w') 
file.writelines((List)) 
file.close() 
  
# Using readline() 
file = open('AboutPython.txt', 'r') 
count = 0
  
while True: 
    count += 1
  
    # Get next line from file 
    line = file.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line{}: {}".format(count, line.strip())) 
  
file.close()

```
---

## Task 10. Write a python code using class (at least 3 functions inside) and dictionary.

```python
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

```
---
