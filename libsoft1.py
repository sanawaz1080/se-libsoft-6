import os
def createfile():
    filename=open("rollno.txt","w")
    filename.write("P Chandra Prakash Babu")
    filename.close()
    return filename
p=input(" p enter the number")   
class account:
    def __init__(self,number,roll="234"):
        self.number=number;
        self.roll=roll;
    def change(self):
        if self.roll==input("for change enter the rollnumber"):
            f=createfile()
            f=open("rollno.txt","r")
            data=f.read()
            print(data)
        if self.number==int(input(" for change enter the id")):
            f1=open("libsoft1.txt","a")
            f1.write(data+" "+p+" "+input("enter the data"))
            f1.close()
    def returnbook(self):
        print("return the book\n")
        if input("book return code")==p and self.number==int(input("enter the number code")) and self.roll==input("enter the roll number"):
            os.remove("libsoft1.txt")
obj=account(int(input("enter the number code")),input("enter the roll number"))
obj.change()
obj.returnbook()