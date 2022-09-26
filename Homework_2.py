#JESUS CHAVEZ // COSC 4600
#IMPORTANT INFORMATION: I made it take user input so that test cases are easier to test
def vacuum_world():
    
    #Initializing our goal; Room checked and cleaned = 'done'.
    goal = {'A': 'done', 'B': 'done'} 

    #Initialize our performance measurment variable.
    performance = 0 

     #Ask user where vacuum is first placed.
    initial_location = input("Enter Location of Vacuum: ")

    #If user puts the vacuum in A first, it will ask satus of A then B.
    if initial_location == ('A' or 'a'):
        initial_location_status = input("Enter status of A: ")
        second_location_status = input("Enter status of B: ")

    #If user puts the vacuum in B first, it will ask satus of B then A.
    if initial_location == ('B' or 'b'):
        initial_location_status = input("Enter status of B: ")
        second_location_status = input("Enter status of A: ")

    #This code will allow you to hard code the initial location and the room status'
        #initial_location = 'A'
        #second_location = 'B'
        #initial_location_status = 'CLean'
        #second_location_status = 'Dirty'

    #Initial location chosen = A
    if initial_location == 'A' or initial_location == 'a':
        print("Vacuum is placed in Location A")

        #If location A is chosen first and is dirty; It will suck up dirt, clean the location and move onto location B
        if initial_location_status == 'dirty' or initial_location_status == 'Dirty':
            print("Location A is dirty.")
            goal['A'] = 'done'
            print("Sucking up the dirt.")
            #Performance increase by 10 points for cleaning
            performance += 10 
            print("Location A has been cleaned (+10 pts).")
            print("Moving right to location B (-1).")
            #Performance decrease by 1 point for changing rooms
            performance -= 1 
        
        #If location A is chosen first and is clean; It will move onto location B
        if initial_location_status == 'Clean' or initial_location_status == 'clean':
            print("Location A is already clean ")
            print("Moving right to location B (-1).")
            #Performance decrease by 1 point for changing rooms
            performance -= 1 

        #Now we moved to location B and it is dirty; It will suck up dirt, clean the location and finish
        if second_location_status == 'dirty' or second_location_status == 'Dirty':
            print("Location B is dirty.")
            goal['B'] = 'done'
            print("Sucking up the dirt.")
            #Performance increase by 10 points for cleaning
            performance += 10
            print("Location B has been cleaned (+10 pts).")
        else:
             #Now we moved to location B and it is clean; No action
            print("Location B is already clean.")
            print("No action")

    #Initial location chosen = B
    else:
        print("Vacuum is placed in location B")

         #If location B is chosen first and is dirty; It will suck up dirt, clean the location and move onto location A
        if initial_location_status == 'dirty' or initial_location_status == 'Dirty':
            print("Location B is dirty.")
            goal['B'] = 'done'
            print("Sucking up the dirt.")
            #Performance increase by 10 points for cleaning
            performance += 10 
            print("Location B has been cleaned (+10 pts).")
            print("Moving left to location A (-1).")
            #Performance decrease by 1 point for changing rooms
            performance -= 1 

         #If location B is chosen first and is clean; It will move onto location A
        if initial_location_status == 'Clean' or initial_location_status == 'clean':
            print("Location B is already clean ")
            print("Moving left to location A (-1).")
            #Performance decrease by 1 point for changing rooms
            performance -= 1 

        #Now we moved to location A and it is dirty; It will suck up dirt, clean the location and finish
        if second_location_status == 'dirty' or second_location_status == 'Dirty':
            print("Location A is dirty.")
            goal['A'] = 'done'
            print("Sucking up the dirt.")
            #Performance increase by 10 points for cleaning
            performance += 10 
            print("Location A has been cleaned (+10 pts).")

        else:
            #Now we moved to location A and it is clean; No action
            print("Location A is already clean.")
            print("No action.")

    #Print out the Performance Score
    print("Performance Score: " + str(performance))

vacuum_world()