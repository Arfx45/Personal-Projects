# CPS 109 Assignment #1
# Name: Arnab Nath
# Student ID: 501165959
# MarkBook Appplication
## Simple application that can store marks and for a student and ouputs the final result interm of the total calculated averages##


import math #Inputs that exist for effiency
import sys
def assignmentUpdates(x,n): #function that stores the grades  into lists
    i=1
    print("\u001bc", end="") #clear terminal function
    print("\nInput your marks for your "+n+"'s\n\nTo stop either type break or stop\n") #user info
    while  True: #iterator that stores values until the user types stop or back
        
        print("Enter your Mark for "+n+" #"+str(i)+" :")
        mark= input() #input
        if mark.upper() == "STOP" or mark.upper() == "BACK": #if statements to check if the input is valid
            break
        elif(float(mark)>=0 and float(mark)<=100):
            x.append(mark)
            i+=1
        else:
            print("\nTHE INPUT NOT EXCEPTED PLEASE ENTER A VALID INPUT!! ")

def updateFinal(t): # Function to get the final value from the user
    print("\u001bc", end="") #clear terminal function
    t= input("Enter your Exam Mark: ") # takes input
    if float(t)>=0 and float(t)<=100:
        return t #reuturs the value if conditions are met

    else:
        print("Please Input a valid number between 0-100")

def getAvg(x):  # Fuction to get the average of our list with the values
    sum=0
    if len(x)>0:
        for i in x: #iteartor to go through every value and get the sum
            sum+=float(i)
        return round(float(sum/len(x)), 2) #return the sum divided by the size of the list
    else:
        return 0
    
def outPrint (z,which): #prints out each list as the format suggests
    print("--"+which+"s-------------------------")
    file.write("--"+which+"s-------------------------\n")
    for i in range (len(z)): #Iterator print out every value of the list
        print("| "+which+" #"+str(i+1)," | "+str(z[i])+"%  |\n")
        file.write("| "+which+" #"+str(i+1)+" | "+str(z[i])+"%  |\n") #stores into the text file
        
    print ("| "+which+"'s Average |  "+str(getAvg(z))+"%  |\n")
    file.write("| "+which+"'s Average |  "+str(getAvg(z))+"%  |\n")# the avg of the list stored to our text file
def finalAvg(q,a,t,f):
    quiz= 15.0      # wheitage of each value
    tst= 20.0
    assi=20.0
    fin = 45
    tot=0.0 #value student achived
    outof=0 # total value possible
    if len(q)>0 : #iterator to see if any value exists in the list and if yes add the average to our final sum acording to the weigh fator of the List
        m= getAvg(q)/100
        tot+= m*quiz
        outof+=quiz
    if len(a)>0 : # same as the last one 
        m= getAvg(a)/100
        tot+= m*assi
        outof+=assi
        
    if len(t)>0 :
        m= getAvg(a)/100
        tot+= m*tst
        outof+=tst
    if f!=0  :
        m= getAvg(a)/100
        tot+= m*fin
        outof+=fin   

    if outof>0: # checking if the total value is greater that zero to avoid zero division error case
        fin = round((tot/outof)*100,2)
    else:
        fin = 0 
    print("| Final Average  |  "+str(fin)+"%  |\n") 
    file.write("| Final Average  |  "+str(fin)+"%  |\n") #storing the final value into our list
if __name__=="__main__": # start of the main fucntion
    assignment = [] #initation of lists and Variables
    test = []
    quizes = []
    final = 0
    while True: #loop to start our fucntion 
        file = open("output.txt","w") #opening the file here so every time we come back to the main menu we have aceess to editing the file
        print("\u001bc", end="") #clear terminal function
        print ("----------------------------\nWelcome to Markbook \nSelect One Of The Menu Options") #UI

        print("-----------------------------\n --> Update Grades\n --> Printout\n --> Exit")#UI
        j = input()#taking input for user action
        if j.upper()== "EXIT": #leaving the program
            print("\u001bc", end="") #clear terminal functionbreak
            break
            
        elif(j.upper() == "PRINT"):
            
            print("\u001bc", end="") #clear terminal function
            print("-----------Current Prinout------------\n")
            file.write("-----------Current Prinout------------\n")#ui for file
            outPrint(assignment,"Assignment") #going into our methods
            outPrint(test,"Test")#going into our methods
            outPrint(quizes,"Quizes")#going into our methods
            finalAvg(quizes,assignment,test,final)#going into our methods
            file.close()#closing file when done
            
            t=input("\n--> Back\n")
            if t.upper() == "BACK":
                pass
            
        else:
            while True: 
                print("\u001bc", end="") #clear terminal function
                print("-----------GRADES------------\n")#going into editing the values of our list
                print("--> Assignements\n--> Quizzes\n--> Tests\n--> Final\n--> Exit")
                s=input("Select One of the options Stated above: ") #selecting options

                if s.upper() == "ASSIGNMENT" or s.upper() == "A": #for assignments
                    assignmentUpdates(assignment, "Assignment")
                elif s.upper() == "QUIZES" or s.upper() == "Q":#for quizzes
                    assignmentUpdates(quizes, "Quiz")
                elif s.upper() == "TEST" or s.upper() == "T":#for Tests
                    assignmentUpdates(test, "Test")
                elif s.upper() == "FINAL" or s.upper()=="F":#for Final
                    final = updateFinal(final)
                elif s.upper()== "EXIT" or s.upper()== "BACK": #exiting back into the menu
                    break

                

