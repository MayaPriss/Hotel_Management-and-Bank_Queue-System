import sys
class Customer:
# Constructor
    def __init__(self):
        self.name = ''  
        self.phone = ''
        self.address =  ''  
        self.cindate = '' 
        self.coutdate = '' 
        self.s = 0
    
    # Function to take input of customer details
    def setCustomer(self):
        self.name = input("Enter Your Name: ")
        self.phone = int(input("Enter Your Phone Number: "))   
        self.address = input("Enter Your Address: ")
        self.cindate = input("Enter Your Check-in date: ")
        self.coutdate = input("Enter Your Check-out date: ")
     
    # Function to book room
    def bookRoom(self):
        print ("We have the following rooms for you:-")
        print ("1. Economic Single Bed  -->  RM 200")
        print ("2. Single Bed luxury    -->  RM 220")
        print ("3. Large Room King Size -->  RM 250")
        print ("4. Suite Room           -->  RM 300")
        
        x = int(input("Enter Your Choice Please -> "))
        n = int(input("How Many Nights Do You Want To Stay? : "))
        
        if(x==1):
            print ("You have opted room type - Economic Single Bed ")
            self.s=200*n

        elif (x==2):
            print ("You have opted room type - Single Bed luxury ")
            self.s=220*n

        elif (x==3):
            print ("You have opted room type - Large Room King Size ")
            self.s=250*n

        elif (x==4):
            print ("You have opted room type - Suite Room")
            self.s=300*n

        else:
            print ("Wrong choice !!!")
            print ("Your room rent is =",self.s,"\n")
     
    # Function for payment
    def Payment(self):
        print(" Payment")
        print("  MODE OF PAYMENT")
           
        print("  1- Credit/Debit Card")
        print("  2- Paytm/PhonePe")
        print("  3- Using UPI")
        print("  4- Cash")
        
        ch=int(input("-> "))
        print("\n  Amount: ",self.s)
        print("\n            PAY FOR JADE")
        print("  (y/n)")
        ch=str(input("->"))
        if ch=='y' or ch=='Y':
            print("          HOTEL JADE")
            print("             Bill")
            print(" Name: ",self.name,"\t\n Phone Number: ",self.phone,"\t\n Address: ",self.address,"\t")
            print("\n Check-In: ",self.cindate,"\t\n Check-Out: ",self.coutdate,"\t")
            print("\n Total Amount: ",self.s,"\t")
            print("          Thank You")
            print("          Visit Again :)")
            
    # Function to display customer details  
    def displayCustomer(self):
        print("Name: ",self.name)
        print("Phone Number: ",self.phone)
        print("Address: ",self.address)
        print ("Check in date: ",self.cindate)
        print ("Check out date: ",self.coutdate)
        print ("Your grandtotal bill is:",self.s,"\n")

        
    
#Driver code
# Create a list to add Customers
ls =[]
while(True):
  
    print("\nWELCOME TO JADE HOTEL ")
    print("\n1. Enter Customer Details\n2. Book Room \n3. Display Customer Details\n"
       "4. Sort Customer Details \n5. Delete Customer Details"
       "\n6. Exit")
    
    
    
    ch = int(input("Enter choice: "))
    if(ch == 1):
        obj = Customer()
        obj.setCustomer()
        ls.append(obj)
        
    elif(ch == 2):
        for i in range(ls.__len__()): 
            print("\t",ls[i].phone)
            ls[i].bookRoom()
            ls[i].Payment()
            break
                               
    elif(ch == 3):
        print("\n")
        print("\nList of Customers\n")
        for i in range(ls.__len__()):     
            ls[i].displayCustomer()
             
    elif(ch == 4):
        print("\n Customer List (Ascending) ")
        newCustomer = sorted(ls, key=lambda x: x.name)
        for customer in newCustomer:
            print(customer.displayCustomer())
    
    elif(ch == 5):
        print("Enter Phone No :", end = " ")
        phone = int(input())
        for i in range(ls.__len__()):
            if ls[i].phone == phone:
                ls.remove(ls[i])
                break
        print("List after deletion")
        for i in range(ls.__len__()):     
            ls[i].displayCustomer()
             
    else:
        print("Thank You !")
        sys.exit()

