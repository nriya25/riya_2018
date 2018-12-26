import getpass
import time
def login() :
        acc = int(input("Login Id:"))
        time.sleep(1)
        passwd= getpass.getpass()
        time.sleep(1)
        if acc in bank['acc'] :
            i = bank['acc'].index(acc)
            if passwd==bank['password'][i] :
                print("******processing*******")
                time.sleep(2)
                print("\n\n1.Debit\n2.Credit\n3.Check balance")
                ch=int(input("choice:"))
                if ch == 1 :
                    amount = int(input("Enter amount to withdraw:"))
                    if amount > bank['bal'][i] :
                        print("\n\n Insufficient amount")
                    else :
                        bank['bal'][i] -= amount
                        time.sleep(1)
                        print("\n{} rs withdrawn from your account".format(amount))
                        print("remaining balance is ",bank['bal'][i])
                elif ch == 2 :
                    amount = int(input("Enter amount to add to your account:"))
                    bank['bal'][i] += amount
                    print("Your request is processing")
                    time.sleep(2)
                    print("\n{} Rs added to your account".format(amount))
                    print("Your current balance is ",bank['bal'][i])
                elif ch == 3 :
                    print("your account balance is:",bank['bal'][i])
                else :
                    print("\n\n Invalid choice")
            else :
                print("\n\nInvalid password try again")

        else :
            print("\n No such user exists")
            print("\n you can signup")
def signup():
        name=input("\n\n enter name")
        time.sleep(1)
        password=getpass.getpass()
        time.sleep(1)
        bal=int(input("initial deposit amount"))
        time.sleep(1)
        acc=bank['acc'][-1] + 1
        bank['name'].append(name)
        bank['password'].append(password)
        bank['acc'].append(acc)
        bank['bal'].append(bal)
        print("your account successfully created")
        print("note your account number: {}".format(acc))

bank={'name':['john','hari','jadu'],
        'acc':[1001,1002,1003],
        'bal':[10000,20000,30000],
        'password':['abcd','xyz','redhat']}
while input("press any key to continue") :
    print("\n\n1.LOgin\n2.Signup\n")
    ch=int(input("your choice"))
    print("********Processing*******\n")
    time.sleep(2)
    if ch == 1 :
        login()
    elif ch==2:
        signup()
    else :
        print("invalid code")
