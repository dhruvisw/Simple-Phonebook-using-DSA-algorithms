import sys
 
import os


 
def create():
 
    file=open('contact.txt','a')
 
    condition='y'
 
    while(condition=='y' or condition=='Y'):
 
        name=input("Name: ")
 
        num=input("Contact Number: ")
 
        email=input("Email ID: ")
 
        file.write( name + '\n')
 
        file.write( num + '\n')
 
        file.write( email + '\n')
 
        file.write("------------------------------------" + '\n')
 
        condition=input("Do you want to enter another contact? Y or N:  ")
 
    file.close()
 
 
 
def edit():
 
    file2=open('contact.txt','r')
 
    temp=open('tempfile.txt','w')
 
    name=input("Enter the name to edit the contact's details: ")
 
    contactnew=input("Enter new Contact Number: ")
 
    emailnew=input("Enter new Email ID: ")
 
    descr=file2.readline()
 
    found=False
 
    while(descr != ''):
 
        contact=file2.readline()
 
        email=file2.readline()
 
        dash=file2.readline()
 
        if(name in descr):
 
            temp.write(descr)
 
            temp.write(contactnew+'\n')
 
            temp.write(emailnew+'\n')
 
            temp.write(dash)
 
            found=True
 
        else:
 
            temp.write(descr)
 
            temp.write(contact)
 
            temp.write(email)
 
            temp.write(dash)
 
        descr=file2.readline()
 
 
 
    temp.close()
 
    file2.close()
 
    if found:
 
        print("Found and changed")
 
    else:
 
        print("Contact was unfound")
 
    os.remove('contact.txt')
 
    os.rename('tempfile.txt','contact.txt')
 
 
 
 
 
def show():
 
    file3=open('contact.txt','r')
 
    for line in file3:
 
        print (line)
 
 
 
def search():
 
    file4=open('contact.txt','r')
 
    flag=1
 
    name=input("Search Name:")
 
    for line in file4:
 
        if(name in line):
 
            contact=file4.readline()
 
            emailid=file4.readline()
 
            print ('Name : ' + name + '\n')
 
            print ('Contact Number : ' + contact + '\n')
 
            print ('Email ID : ' + emailid + '\n')
 
            flag=0
 
    if(flag==1):
 
        print("Contact with the entered name was unfound :( \n")
 
 
 
def delete():
 
    file2=open('contact.txt','r')
 
    temp=open('tempfile.txt','w')
 
    name=input("Enter the name whose contact you want to delete: ")
 
    descr=file2.readline()
 
    found=False
 
    while(descr != ''):
 
        contact=file2.readline()
 
        email=file2.readline()
 
        dash=file2.readline()
 
        if(name in descr):
 
            found=True
 
        else:
 
            temp.write(descr)
 
            temp.write(contact)
 
            temp.write(email)
 
            temp.write(dash)
 
        descr=file2.readline()        
 
    temp.close()
 
    file2.close()
 
    if found:
 
        print("\nFound and Deleted")
 
    else:
 
        print("Contact Not Found")
 
    os.remove('contact.txt')
 
    os.rename('tempfile.txt','contact.txt')
 
 
 
def end():
 
    sys.exit()
 
 
 
condition='y'
 
while(condition=='y' or condition=='Y'):    
 
    os.system('cls')
 
    print("\n**************  PYTHON PHONE DIRECTORY APPLICATION  ***************\n-3501 Dhruvi\n-3506 Aishani\n-3512 Kedar")
 
    print("\n1. Create a new Contact")
 
    print("2. Display Contacts")
 
    print("3. Edit Contacts")
 
    print("4. Remove Contacts")
 
    print("5. Search")
 
    print("6. End")
 
    choice=int(input("\nSelect an option: "))
 
    if(choice==1):
 
        create()
 
    elif(choice==2):
 
        show()
 
    elif(choice==3):
 
        edit()
 
    elif(choice==4):
 
        delete()
 
    elif(choice==5):
 
        search()
 
    elif(choice==6):
 
        end()
 
    condition=input("\nWould you like to continue? Y or N: ")