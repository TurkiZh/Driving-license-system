# This word done by group 12
# Turki, 202041480, 50%
# Jehad, 202026100, 50%
def main(): # we start the program
    option = "0"
    exit = 1        
    while option != "7":
        menu()
        option = input()
        if option == "1": # add new person option
            listOfAddingPerson = addingPerson() # call the adding person function
            persons = open("persons.txt","a")
            for info in listOfAddingPerson:
                persons.write("%-12s"%info)
            persons.write("\n")
            persons.close()
                                    
        elif option == "2": #  Display information of all persons
            print("%36s"%"1.   Sort by ID")
            print("%44s"%"2.   Sort by First Name")
            print("%40s"%"3.   Sort by Gender")
            choice = input("Enter your Choice: ")
            infoOFallpersons(choice)
            
        elif option == "3": # Display information of a specific person (Update - Delete)
            infoForSpecific()
            
        elif option == "4": #  Issue/Renew license
            listOfLicense = renewLicense()
            license = open("licenses.txt","a")
            for info in listOfLicense:
                license.write("%-22s"%info)
            license.write("\n")
            license.close()

        elif option == "5":  #  Display licenses information
            displayLicenses()
                
        elif option == "6": # Display expired-soon licenses information
            expiredSoonLicenses()
            
        elif option == "7": # Exit
            print("Exit The program")
                
        else:
            print("Error, Enter a Valid Choice")

def menu(): # We call the menu function to print all Options
    print("#"*123)
    print("%70s"%"Driving License Management System")
    print("%40s"%"1.   Add New Person")
    print("%60s"%"2.   Display Information or All Persons")
    print("%83s"%"3.   Display Information for A Specific Person (Update-Delete)")
    print("%45s"%"4.   Issue/Renew License")
    print("%54s"%"5.   Display Licenses Information")
    print("%67s"%"6.   Display Expired-Soon Licenses Information")
    print("%30s"%"7.   Exit")
    print("Enter your choice: ")
    print("#"*123)
            
def addingPerson(): #  adding person function
    listOfAddingPerson = []
    months31Days = ["1","3","5","7","8","10","12"]
    months30Days = ["4","6","9","11"]
    bloodGroup = ["A+","A-","B+","B-","O+","O-","AB+","AB-","A","B","O","AB"]
    addingID = 1
    addingFName = 0
    addingLName = 0
    addingGender = 0
    addingNation = 0       #  we set all whiles on 0 and change them to 1 when the correct data entered
    addingAddress = 0
    addingDOB = 0
    addingBlood = 0
    addingMobile = 0

    while addingID == 1: # Adding ID now
        checkingID = 0
        personID = input("Enter the ID: ")
        addingFile = open("persons.txt", "r")
        if len(personID) == 4:
            if personID.isdigit():
                for line in addingFile:
                    split = line.split()
                    for word in split:
                        if personID == word:
                            checkingID = checkingID + 1
                if checkingID == 0:
                    addingFile = open("persons.txt", "a")
                    print("ID is Added Successfully!")
                    listOfAddingPerson.append(personID)
                    addingFName = 1
                    addingID = 0
                elif checkingID >= 1:
                    print("ID exists already.")       #  when the correct data entered we make th while False
                    addingID = 0
                    exit = 0
            else:
                print("Error, ID Number must contain digits only!")
        else:
            print("Error, ID Number must be 4 digits!")

    while addingFName == 1:         # adding the first name 
        personFName = input("Enter the First Name: ")
        if personFName.isalpha():
            print("First Name is Added Successfully!")
            listOfAddingPerson.append(personFName.capitalize())
            addingFName = 0                      # when the correct data entered we make the loop false
            addingLName = 1                      #  so we move to the next part
        else:
            print("Error, First Name must contain at least 1 letter with no Digits!")

    while addingLName == 1:        # this is adding the last name loop
        personLName = input("Enter the Last Name: ")
        if personLName.isalpha():
            print("Last Name is Added Successfully!")
            listOfAddingPerson.append(personLName.capitalize())
            addingLName = 0             # it will not stop until valid name entered
            addingGender = 1
        else:
            print("Error, Last Name must contain at least 1 letter with no Digits!")

    while addingGender == 1:    # this is adding gender
        personGender = input("Enter the Gender (Male-Female): ")
        if personGender.upper() == "MALE" or personGender.upper() == "FEMALE":
            print("Gender is Added Successfully!")
            listOfAddingPerson.append(personGender.capitalize())
            addingGender = 0        # it will stop only when the user write male or female
            addingNation = 1
        else:
            print("Error, Gender must be either Male or Female!")

    while addingNation == 1:        # adding nation
        personNation = input("Enter the Nationality: ")
        if personNation.isalpha():
            print("Nationality is Added Successfully!")
            listOfAddingPerson.append(personNation.capitalize())
            addingNation = 0
            addingAddress = 1
        else:
            print("Error, National is Invalid")

    while addingAddress == 1:           # this is adding address it only accepts letters
        personAddress = input("Enter the Address: ")
        if personNation.isalpha():
            print("Address is Added Successfully!")
            listOfAddingPerson.append(personAddress.capitalize())
            addingAddress = 0
            addingDOB = 1
        else:
            print("Error, Address must contain letter with no Digits!")

    while addingDOB == 1:        # adding the date of birth only accepts numbers
        dobYear = input("Enter the Year of birth: ")
        if dobYear.isdigit():
            if int(dobYear) <= 2021 and int(dobYear) >= 1920:  # the date of birth will not allow a user to enter invalid year
                dobMonth = input("Enter the Month of birth: ") #  such as 1900 or 2030
                if dobMonth.isdigit():
                    if dobMonth in months31Days:
                        dobDay = input("Enter the Day of birth: ")
                        if int(dobDay) >= 1 and int(dobDay) <= 31:
                            print("Date of birth is added successfully!")
                            dob = dobDay + "/" + dobMonth + "/" + dobYear
                            listOfAddingPerson.append(dob)
                            addingDOB = 0
                            addingBlood = 1
                        else:
                            print("Error, Invalid Date!")
                    elif dobMonth in months30Days:      # also the days limit depends on the month if the month has
                        dobDay = input("Enter the Day of birth: ") #  31 or 30 or 29 days
                        if int(dobDay) >= 1 and int(dobDay) <= 30:
                            print("Date of birth is added successfully!")
                            dob = dobDay + "/" + dobMonth + "/" + dobYear
                            listOfAddingPerson.append(dob)
                            addingDOB = 0
                            addingBlood = 1
                        else:
                            print("Error, Invalid Date!")
                    elif dobMonth == "2":   # this month has 29 days so it will accept only days till 29
                        dobDay = input("Enter the Day of birth: ")
                        if int(dobDay) >= 1 and int(dobDay) <= 29:
                            print("Date of birth is added successfully!")
                            dob = dobDay + "/" + dobMonth + "/" + dobYear
                            listOfAddingPerson.append(dob)
                            addingDOB = 0
                            addingBlood = 1
                        else:
                            print("Error, Invalid Date!")
                    else:
                        print("Error, Invalid Date!")
                else:
                    print("Error, Invalid Date!")       # these errors will show if the user entered wrong input
            else:
                print("Error, Invalid Date!")
        else:
            print("Error, Invalid Date!")

    while addingBlood == 1:     # adding blood will accept only the known blood group such as B+,O-,AB+
        personBlood = input("Enter the Blood Group (X+,X-): ")
        if personBlood.upper() in bloodGroup:
            listOfAddingPerson.append(personBlood.capitalize())
            addingBlood = 0
            addingMobile = 1
        else:
            print("Error,Invalid Blood group")

    while addingMobile == 1:   # adding mobile will accept only numbers and 10 numbers must be enterd
        personMobile = input("Enter the Mobile Number (05********): ") # or it will be (short-long)
        if len(personMobile) == 10:
            listOfAddingPerson.append(personMobile)
            print("Person's data are Successfully Added!")
            addingMobile = 0
        elif len(personMobile) > 10:
            print("Error, Too Long")
        elif len(personMobile) < 10:
            print("Error, Too Short")
            
    return listOfAddingPerson

def infoOFallpersons(entered_value):
    print()
    #here we are reading the file and put the lines in lists then we put them in dictionary.
    forSortting = {}
    toOpen= open("persons.txt","r")
    toOpen.readline()
    for line in toOpen:
        info = line.split()
        forSortting[info[0]] = {"FirstName": info[1],"LastName": info[2], "Gender": info[3], "Nationality": info[4], "Address": info[5], "DOB": info[6], "BloodGroup": info[7], "MobileNumber": info[8]}
    #here we have 3 choices each one is to sort by ID , Frist name or gender .
    if entered_value == "1" :
        sortChoice = sorted (forSortting.keys())
    elif entered_value == "2":

        sortChoice = sorted(forSortting, key=lambda x: forSortting[x]["FirstName"])
    else :
        if entered_value == "3" :
            sortChoice = sorted(forSortting, key=lambda x: forSortting[x]["Gender"])
    #here we print the choice that entered by the user.
    for i in sortChoice:
        print (i,forSortting[i]["FirstName"] ,forSortting[i]["LastName"],forSortting[i]["Gender"],forSortting[i]["Nationality"],forSortting[i]["DOB"],forSortting[i]["BloodGroup"],forSortting[i]["MobileNumber"])
    print()
    print()

def infoForSpecific():
    

    #here we are reading the file and put the lines in lists then we put them in dictionary.
  
    forInserting_1 = {}
    toOpen_1=  open('licenses.txt','r')
    toOpen_1.readline()
    
    for line_1 in toOpen_1:
        data_1 = line_1.split()
        forInserting_1[data_1[0]] = {"Fee": data_1[1], "Issue Date": data_1[2], "Expiry Date": data_1[3],"Issue Number": data_1[4]}




    forInserting = {}
    toOpen=  open('persons.txt','r')
    toOpen.readline()
    
    for line in toOpen:
        data = line.split()
        
        forInserting[data[0]] = {"FirstName": data[1],"LastName": data[2], "Gender": data[3], "Nationality": data[4], "Address": data[5], "DOB": data[6], "BloodGroup": data[7], "MobileNumber": data[8]}
    toOpen.close()
    #those varble for stopping loops 
    toBreak = 1
    toBreak2 = 1
    toBreak3 = 1
    toBreak4 = 1
    toBreak5 = 1
    #here we creat a except for key error if the input is not in the dictionary.
    try:
     # here we creat list to put values from dictionary and print the data.  
        myList_1 = []
        myList = []
        
        iD = input("Enter ID: ")
        
        
        
        storingValues= forInserting[iD].values()
       
        for values in storingValues:
            myList.append(values)
        print("ID:",iD)
        print("First Name:",myList[0])
        print("Last Name:",myList[1])
        print("Gender:",myList[2])
        print("Nationality:",myList[3])
        print("Address:",myList[4])
        print("DOB:",myList[5])
        print("Blood Group:",myList[6])
        print("Mobile:",myList[7])
        if iD in forInserting_1  :
            storingValues_1= forInserting_1[iD].values()
            for values_1 in storingValues_1:
                myList_1.append(values_1) 
            
            print("Fees Collected: ",myList_1[0])
            print("License Issue Date: ",myList_1[1])
            print("License Expiry Date: ",myList_1[2])
            print("Issue number: ",myList_1[3])
        else : 
            pass
        
        
        # here list of choices that can user do what he want.
        while toBreak5 == 1 : 
            print()
            print("%40s"%"1. Update person information")
            print("%40s"%"2. Delete person information")
            print("%36s"%"0. Back to the main menu")
            print()
            
            userChoice=input("Enter you choice: ")
            #here choice 1 the user will got 4 inputs to update data. 
            if userChoice == "1":
                
                print("Current First Name:",myList[0]) 
                while toBreak == 1:
                    personFName = input("Enter new First Name: ")
                    if personFName.isalpha():
                        toBreak = 0
                    elif personFName == "":
                        toBreak = 0
                    else:
                        print("Error, First Name must contain at least 1 letter with no Digits!")


                if personFName == "" :
                    pass
                else : 
                    forInserting[iD]["FirstName"]= personFName



                print("Current Last Name:",myList[1])
                while toBreak2 == 1:
                    personLName = input("Enter new Last Name: ")
                    if personLName.isalpha():
                        toBreak2 = 0
                    elif personLName == "":
                        toBreak2 = 0
                    else:
                        print("Error, Last Name must contain at least 1 letter with no Digits!")

                if personLName == "" :
                    pass
                else : 
                    forInserting[iD]["LastName"]= personLName

                # we put some conditions like the input must be without digits and the length of mobile phone.

                print("Current Address:",myList[4])    
                while toBreak3 == 1:
                    personAddress = input("Enter new Address: ")
                    if personAddress.isalpha():
                        toBreak3 = 0
                    elif personLName == "":
                        toBreak3 = 0
                    else:
                        print("Error, Address must contain at least 1 letter with no Digits!")  


                if personAddress == "" :
                    pass
                else : 
                    forInserting[iD]["Address"]= personAddress



                print("Mobile:",myList[7])    
                while toBreak4 == 1:
                    personMobile = input("Enter the Mobile Number (05********): ")
                    if len(personMobile) == 10:
                        toBreak4 = 0
                    elif len(personMobile) > 10:
                        print("Error, Too Long")
                        
                    elif 0 < len(personMobile) < 10:
                        print("Error, Too Short")
                        
                    elif len(personMobile) == 0 :
                        toBreak4 = 0

                if personMobile == "" :
                    pass
                else : 
                    forInserting[iD]["MobileNumber"]= personMobile
                print("Person's data has been updated!")
                toBreak5 = 0
            #here choice 2 to remove all data of the user selected. 
            elif userChoice == "2" :
                forInserting.pop(iD)
                if iD in forInserting_1  : 
                    forInserting_1.pop(iD)
                toBreak5 = 0
                print("Person's data has been deleted!")
            #here choice 3 if the user want to return to the main menu.
            elif userChoice == "0" :
                toBreak5 = 0
                
            else :
                print("Enter a valid choice or press 0 to back to main menu !")
        # this block is to rewrite the data to file after changing data.
        toDel = open("persons.txt","w")
        toDel.close()
        toWrite = open("persons.txt","a")
        toWrite.write("\n")
       
        for ID in forInserting:
            
            toWrite.write("%-12s%-12s%-12s%-12s%-12s%-12s%-12s%-12s%-12s\n"%(ID,forInserting[ID]["FirstName"],forInserting[ID]["LastName"],forInserting[ID]["Gender"],forInserting[ID]["Nationality"],forInserting[ID]["Address"],forInserting[ID]["DOB"],forInserting[ID]["BloodGroup"],forInserting[ID]["MobileNumber"]))

        toWrite.close()
        
        
        toDel_1 = open("licenses.txt","w")
        toDel_1.close()
        toWrite_1 = open("licenses.txt","a")
        toWrite_1.write("\n")
       
        for ID_1 in forInserting_1:
            
            toWrite_1.write("%-12s%-12s%-12s%-12s%-12s\n"%(ID_1,forInserting_1[ID_1]["Fee"],forInserting_1[ID_1]["Issue Date"],forInserting_1[ID_1]["Expiry Date"],forInserting_1[ID_1]["Issue Number"]))

        toWrite.close()
        
               

        
    except KeyError :
        print("ID not Found. returning to menu!")       

def renewLicense():  # renew license function
    import datetime  # first we import the current date from the device
    
    gg = {}
    toOpen=  open('licenses.txt','r')
    toOpen.readline()
    
    for line in toOpen:
        data = line.split()
        gg[data[0]] = {"Fee": data[1],"Issue Date": data[2], "Expiry Date": data[3], "Issue Number": data[4]}
    toOpen.close()
    
    
    x = datetime.datetime.now()
    issueYear = str(x.year)
    issueMonth = str(x.month)
    issueDay = str(x.day)
    issueDate = str(x.day) + "/" + str(x.month) + "/" + str(x.year) # we define the issue date with the current date
    personsFile = open("persons.txt","r")      # first we open the persons file to check if the id exist there
    personID = input("Enter the ID: ") 
    listOfLicense = []
    renewID = 1
    deletingID = 0
    issueDateloop = 0
    findIssueNumber = 0
    addingLicenseList = 0
    findLicense = 0
    findID = 0
    while renewID == 1:
        if len(personID) == 4:
            if personID.isdigit():
                for line in personsFile:
                    split = line.split()   # to check the ID if it has 4 digits ONLY.
                    for word in split:
                        if personID == word:
                            findID += 1
            else:
                print("Error, ID Number must contain digits only!")
        else:
            print("Error, ID Number must be 4 digits!")
        while renewID == 1:
            if findID >= 1:
                print("%30s"%"Fee","%36s"%"Licence duration in years")  # display to the user the options of fee
                print("%30s"%"100","%12s"%"2")
                print("%30s"%"200","%12s"%"4")
                print("%30s"%"400","%13s"%"10")
                feeChoice = input("Enter The Fee: ")   # we ask which fee the user want to pay
                while renewID == 1:
                    if feeChoice == "100" or feeChoice == "200" or feeChoice == "400":
                        renewID = 0
                        findIssueNumber = 1
                    else:
                        print("Invalid input, Back to main menu")
                        renewID = 0    # if user entered wrong fee it will bring him back to main menu
                        
            else:
                print("ID Number Does Not Exist!")
                renewID = 0
    personsFile.close()

    while findIssueNumber == 1:   # to find the issue number if it's not the first time to renew the license for an ID
        licenseFile = open("licenses.txt","r")
        licenseFile.readline()
        for line in licenseFile:
            split = line.split()
            for word in split:
                if personID == word:
                    findLicense = 1
        licenseFile.close()
        
        licenseFile = open("licenses.txt","r")
        if findLicense == 0:
            issueNumber = 1
            findIssueNumber = 0
            addingLicenseList = 1
        elif findLicense == 1:
            forSortting = []
            for line in licenseFile:
                info = line.split()
                for word in info:
                    if word == personID:
                        forSortting = [info[0],info[1],info[2],info[3],info[4]]
                        oldIssueNumber = forSortting[4]
                        issueNumber = int(oldIssueNumber) + 1
                        findIssueNumber = 0
                        addingLicenseList = 1
        licenseFile.close()
        
    while addingLicenseList == 1: # these are calculations to collect data such as Fee - Expiry Date - Issue date
        if findLicense == 0:
            if feeChoice == "100":
                expiryYear = int(issueYear) + 2
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            elif feeChoice == "200":
                expiryYear = int(issueYear) + 4
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            elif feeChoice == "400":
                expiryYear = int(issueYear) + 10
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            listOfLicense = [personID,feeChoice,issueDate,expiryDate,"1"]
        elif findLicense >= 1:
            if feeChoice == "100":
                expiryYear = int(issueYear) + 2
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            elif feeChoice == "200":
                expiryYear = int(issueYear) + 4
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            elif feeChoice == "400":
                expiryYear = int(issueYear) + 10
                expiryDate = issueDay + "/" + issueMonth + "/" + str(expiryYear)
            listOfLicense = [personID,feeChoice,issueDate,expiryDate,str(issueNumber)] 
            deletingID = 1
            
        if deletingID == 1:
            gg.pop(personID)
        tt= open('licenses.txt','w')
        tt.write("\n")
        for i in gg :
            tt.write("%-22s%-22s%-22s%-22s%-22s\n"%(i,gg[i]["Fee"],gg[i]["Issue Date"],gg[i]["Expiry Date"],gg[i]["Issue Number"]))
            
        
        print("License is added successfully !")
        addingLicenseList = 0
    
    return(listOfLicense)

def displayLicenses(): # function to display all licenses with fees and dates and other
    print("((Printing All Licenses...))")
    print()
    print("%10s"%"ID","%10s"%"Fee","%16s"%"Issue Date","%16s"%"Expiry Date","%18s"%"Issue Number")
    licensesSort = []
    licensesFile = open("licenses.txt","r")
    licensesFile.readline()
    for line in licensesFile:  # this loop will take each line and put it in a list to print the license data
        info = line.split()
        licensesSort = [info[0],info[1],info[2],info[3],info[4]]
        print("%11s"%licensesSort[0],"%9s"%licensesSort[1],"%16s"%licensesSort[2],"%15s"%licensesSort[3],"%13s"%licensesSort[4])
    print()
    
def expiredSoonLicenses():
    import datetime # import date time from the device
    x = datetime.datetime.now()
    date = str(x.day) + "/" + str(x.month) + "/" + str(x.year) # we define the variable date ti the current day-month-year
    licensesFile = open("licenses.txt","r")
    licensesExpiry = []
    expire1Month = 0
    expire2Months = 0
    expire3Months = 0
    licensesFile.readline()
    for line in licensesFile:
        day = 0
        count = 0
        monthExpiry = ""
        info = line.split()
        licensesExpiry = [info[3]]
        yearExpiry = licensesExpiry[0] 
        if yearExpiry[-4:] == str(x.year) or yearExpiry[-4:] == str(x.year+1): # is the current year equal the expiry year
            count = 1                                                          #  or the next year it will become true
            for month in yearExpiry:             # this will define the month of the expiry date
                if month.isdigit():
                    if day == 0:
                        pass
                    elif day == 1:
                        monthExpiry = monthExpiry + month
                else:
                    day = day + 1
        if count == 1:                    # these are calculations for the month differences between the expire month and current month
            if (int(monthExpiry) - x.month) == 3 and yearExpiry[-4:] == str(x.year):
                expire3Months = expire3Months + 1
            elif (int(monthExpiry) - x.month) == 2 and yearExpiry[-4:] == str(x.year):
                expire2Months = expire2Months + 1
            elif ((int(monthExpiry) - x.month) == 1 or (int(monthExpiry) - x.month) == 0) and yearExpiry[-4:] == str(x.year):
                expire1Month = expire1Month + 1 
            elif (x.month - int(monthExpiry)) == 11 and yearExpiry[-4:] == str(x.year+1):
                expire1Month = expire1Month + 1
            elif (x.month - int(monthExpiry)) == 10 and yearExpiry[-4:] == str(x.year+1):
                expire2Months = expire2Months + 1
            elif (x.month - int(monthExpiry)) == 9 and yearExpiry[-4:] == str(x.year+1):
                expire3Months = expire3Months + 1  
            else:
                pass
    print()
    print("%15s"%"Group","%29s"%"Count")
    print("%27s"%"Expire in a month","%15s"%expire1Month)
    print("%28s"%"Expire in 2 months","%14s"%expire2Months) # noe print all information of expire-soon licenses
    print("%28s"%"Expire in 3 months","%14s"%expire3Months)
    print()
    

main()