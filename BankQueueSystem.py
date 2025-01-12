def new_ticket():                                  
    global next_ticket                        
    tickets.append(next_ticket)                
    next_ticket+=1                            
    

def assign_counter(option):                            
    global counter                         
    global tickets
    key = "Counter "+ str(option)
    if len(tickets)==0:                              
        print("Error: There are no tickets in the queue.")
    else:                   
        counter[key] = tickets.pop(0)          

    
tickets = []                                          

counter = {'Counter 1':'Not assigned','Counter 2':'Not assigned',  
           'Counter 3':'Not assigned','Counter 4':'Not assigned',}

next_ticket = 1001                              

print("Enter 0 to 5 for following options:")           
print("0 -> Issue new ticket number.")
print("1 -> Assign first ticket in queue to counter 1.")
print("2 -> Assign first ticket in queue to counter 2.")
print("3 -> Assign first ticket in queue to counter 3.")
print("4 -> Assign first ticket in queue to counter 4.")
print("5 -> Quit program")

while(True):                                           
    print("\nTickets in queue:",tickets)              
    print("Counter assignment:",counter)   
    option = int(input("Enter your option: "))        
    
    if option == 0:                                   
        new_ticket()
        
    elif option>0 and option<5:                       
        assign_counter(option)
        
    elif option == 5:                                  
        print("Quitting program...\n>>>")
        break
        
    else:                                              
        print("Invalid option, try again...")

