'''Python Script To generate an Acronym word from a given sentence given by the user.
   The user can generate the Acronym's until or unless he wants to exit.
'''

print("\n\n\t\tHi! Welcome to Acronym Generator\n")
print("\t\tPress 1 : To Generate Acronym")
print("\t\tPress 0 : To Exit")
n=input("\n\t\tYour choice: ")
#Asking user to enter his choice between 1 and 0.
while(n!="0"):
    while(n=="1"):
        l=input("\n\t\tEnter the Sentence: ").split(" ")
        l=list(l)

        #Taking group of strings(Sentence) in the form of list 
        
        
        s=""
        for i in l:
        #Running loop in list   
            for j in range(0,len(i)):
                s=s+i[j]
                if j==0:
                    break
        #Running inner loop in every String and adding only first letter to 'S' by using break
        s=s.upper()
        print("\n\t\tAcronym:",s)

        #Making the Acronym to upper case and printing it
        #Asking user his choice again

        print("\n\t\tPress 1 to Continue (or) 0 To Exit")
        n=input("\n\t\tYour choice: ")
        
        #If choice is 0 terminating both loops and program. 

        if n=="0":
            break

        #If wrong choice asking user his choice again(Inner loop).
        
        elif n!="0" and n!="1":
            print("\n\t\tEnter a Valid Option")
            n=input("\n\t\tYour choice: ")
    
    #If wrong choice asking user his choice again(Outer loop).       
    
    if n!="0" and n!="1":
        print("\n\t\tEnter a Valid option")
        n=input("\n\t\tYour choice: ")

#If choice is 0 terminating loop and program.       

if n=="0":
    print("\n\t\tThank you! Visit again")
    print("\t\tHave a Great Day !\n\n")
