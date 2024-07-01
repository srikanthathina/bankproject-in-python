print("="*20)

customernames=["janesmith","iason jordan","david morgan","brain john",'jack swift']
customerpins=['0123','2575','7275','2312','5049']
customerbalances=[10000,20000,30000,40000,50000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

# this statement below helps the program to run continusoly
while True:
    # os.system("cls")
    print("=====================================================================================")
    print("=======================WELCOME TO TIMES BANK=========================================")
    print("*************************************************************************************")
    print("=<< 1. open a new acoount >>=")
    print("=<< 2. Withdraw Money >>=")
    print("=<< 3. Deposit Money >>=")
    print("=<< 4. Check Customers & Balance >>=")
    print("=<< 5. Exit/quit >>=")
    print("********************************************************************************")

    # the below statement takes the choice number from the user.
    choicenumber = input("Select your choice number from the above menu : ")
    if choicenumber == "1":
        print("choice number 1 is selected by the customer")
        # the line below will take the no.of customers from the user.
        Noc = eval (input("Number of customers : "))

        i= i + Noc
        # the if condition will restrict the number of new account to 5.
        if i > 5:
            print("\n")
            print("customer registration excedd reached or customer registration too low")
            i = i - Noc
        else:
            # the while loop wil run according to the no.of customers.
            while counter_1 <=i:
            # these few lines will take information from the customer and then append them too the list.
             name = input("Input fullname:")
             customernames.append(name)
             pin = str(input("please input a pin of your choice : "))
             customerpins.append(pin)
             balance = 0
             deposition = eval (input("please input a value to deposit to start an account : "))
             customerbalances.append(balance)
             print("\nName=", end=" ")
             print(customernames[counter_2])
             print("\name=", end=" ")
             print(customerpins[counter_2])
             print("pin=", end=" ")
             print(customerbalances[counter_2], end=" ")
             print("-/rs")
             counter_1 = counter_1 + 1
             counter_2 = counter_2 + 1
             print("\nyour name is added to customer system")
             print("your pin is added to customer system")
             print("your balance is added to customer system")
             print("------New accounted created successfully !------")
             print("\n")
             print("your name is available on the customes list now : ")
             print(customernames)
             print("\n")
             print("Note! please remember the name and pin")
             print("======================================================================")

            #  this statement below helps the user to go back and to  the start of the program(main menu).
            mainMenu = input("please press enter key to go back to main menu to perform another function or exit ...")
    elif choicenumber == "2":
       j = 0
       print("choice number 2 is selected by the customer")

    #    this while loop will prevent the user using account if the username or pin is wrong.
       while j < 1:
        k = -1  
        name = input("please input name : ")
        pin = input("please input pin : ")
    #    this while loop wil keep the function running when variable k is smaller than length of the 
             # customer list.
        while k < len(customernames) - 1:
         k = k + 1
    #    these two if conditions find where both the name and pin matches/
       if name == customernames[k]:
        if pin == customerpins[k]:
         j = j + 1
        #   these few statement woukd show both the name and pin matche
        print("your current balance:", end=" ")
        print(customerbalances[k], end=" ")
        print("-/rs\n")
       balance = (customerbalances[k])

    # statement below would take the amount to withdraw from user.
       withdrawal = eval(input("input value to withdraw : "))
    # the if condition below would look whether the withdraw is greater then the balance.
       if withdrawal > balance:
    #    this statement below would take a deposition from the customer.
        deposition= eval(input("please Deposit a higher value because your balance is mentioned above is not enough : "))
        # these few atatements would update the value and show the balance to user.
        balance = balance + deposition
        print("your current balance:", end=" ")
        print(balance, end= " ")
        print("-/rs\n")
        # 1000 - 500 = 500
        balance = balance - withdrawal
        print("-\n")
        print("-----------withdraw successfull!------------")
        customerbalances[k] = balance 
        print("your new balance :", balance, end =" ")
        print("-/rs/n/n")
        if j < 1 :
        #    the if condition above would work when the pin or the name is wwrong.
           print("your name and pin does not match!\n")
           break
        # this program would help the user to go back to the start of the program (main menu).
        mainmenu = input("please press enter key to go back to mainmenu to perform another function or exit ...")
    elif choicenumber == "3":
       print("choicenumber 3 is selected by the customer")
       n = 0

    #    the while loop  below would work when the pin or the username is wrong.
       while n < 1:
        k = -1
    #    the while loop below would work when the pin or the username is wrong.
        name = input("please input name : ")
        pin = input("please input pin : ")
    # the two if conditions below would find whther both the pin andname is correct.
       if name == customernames[k]:
        if pin == customerpins[k]:
            n = n + 1
        #   these statements below would show the customer balance and update list values according to 
        #  the deposition made.
            print("your current balance: ", end=" ")
            print(customerbalances[k], end=" ")
            print("-\rs")
            balance == (customerbalances[k])

# this statement below takes the deposittion fromthe customer.
            deposition = eval(input("Enter the value you want to deposit: "))
            balance = balance + deposition 
    # 1000 + 500 = 1500
            customerbalances[k] = balance
            print("\n")
            print("------- deposition successful-----------")
            print("your new balance: ",balance, end=" ")
            print("-/rs\n\n")
       if n < 1:
        print("your name and pin does not match\n")
        break
    # this statment below helps the user to go back  to the start of the progeam (main menu).
       mainmenu = input("please press enter key to go back to aminmenu to perfrom another function or exit ...")
    elif choicenumber == "4":
     print("choice number 4 is selectd by the customer")
    k = 0
    print("custome name list and balances mentioned below :  ")
    print("\n")
    k = k + 1

#    this statement below helps the user to go back to the start of the program (mainmenu).
    mainmenu = input("please press enter key to go back to amin menu to perfrom another function or exit...")
    if choicenumber == "5":
#    this statement would be just showed to the customer.
     print("choice number 5 is selected by the customer")
     print("Thank you for using our banking system!")
     print("\n")
     print("Come again")
     print("Bye bye")
     break

    else:
#  this else function above would work when a wrong function is chosen.
     print("Invalid option is selected by the customer.")
     print("please try again")
#    this statement below helps the user to go back to the start of the program (manimenu)>
mainmenu = input("please press enter key to go back to mainmenu to perform another function or exit ...")









   
   

    








                 








