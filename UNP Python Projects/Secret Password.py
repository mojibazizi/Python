password = ""
while password != "secret":
    password = input("please enter your password: ")
    if password == "secret":
        print("Welcome back!")
    else:
        print("Sorry the password you entered is incorrect, please try again! ")
   