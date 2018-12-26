import os
import time
import shutil
def read() :
    f=input("enter full path of file :")
    if os.access(f,os.F_OK) and os.access(f,os.R_OK) :
        f = open(f)
        data = f.read()
        f.close()
        time.sleep(1)
        print("your data is")
        print(data)
    else :
        print("Invalid path or Permission Denied")
        print("Try Again")
    text()
def write() :
    f=input("enter full path of file :")
    f = open(f,'w')
    print(" Type :wq to save file \n\n")
    while True :
        d=input()
        if d.lower() == ':wq' :
            f.close()
            break
        f.write(d)
        f.write('\n')
        time.sleep(1)
        print("Your data is written")
        print("thank you")
    text()

def append() :
    f=input("enter full path of file:")
    f=open(f,'a')
    print("Type save to save \n\n")
    while True :
        d=input()
        if d.lower() == 'save' :
            f.close()
            break
        f.write(d)
        f.write('\n')
        time.sleep(1)
        print("Data is appended")
        print("Bye Bye")
    text()
def copy(symlinks=None,ignore=None) :
    s=input("enter source path")
    d=input("enter destination path")
    if os.path.exists(s) and os.path.exists(d) :
        shutil.copytree(s,d,symlinks,ignore)
    else :
        shutil.copy(s,d)
    text()

def move() :
    s=input("enter source path")
    d=input("enter destination path")
    if s == d:
        print("Error")
        print("source and destination are same")
    else :
        if os.path.exists(s) and os.path.exists(d) :
            shutil.move(s,d)
            print("File moved successfully")
            print("Thank you")
        else :
            print("path does not exist")
            print("Try again")
    text()

def delete() :
    f=input("enter path of file to be deleted")
    os.unlink(f)
    print("file deleted successfully")
    text()
def change() :
    f=input("enter path to change directory")
    os.chdir(f)
    print("path changed")
    text()
def create() :
    f=input("enter full path of file: ")
    f=os.mkdir(f)
    print("file successfully created")
    print("thank you")
    text()

def text() :
    print("1.Read\n2.Write\n3.Append\n4.Copy\n5.Move\n6.Delete\n7.Change directory\n8.create directory\n9.exit")
    ch=int(input("your choice : "))
    if ch == 1:
        read()
    elif ch == 2 :
        write()
    elif ch == 3:
        append()
    elif ch == 4:
        copy()
    elif ch == 5:
        move()
    elif ch == 6:
        delete()
    elif ch == 7:
        change()
    elif ch == 8 :
        create()
    elif ch == 9:
        exit(0)
    else:
        print("Invalid choice! Please enter valid choice.")
    text()

if __name__ == "__main__" :
    text()
