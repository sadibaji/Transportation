class panel:

    @staticmethod
    def entry_panel():
        username  = "a"
        password = "a"
        print("1-Admin\n2-Train Employee\n3-User\n4-quit")
        entrypanel_selection = input()
        while True:
            if entrypanel_selection == '1':
                panel.admin_login_panel(username, password)

            elif entrypanel_selection == '2':
                panel.employee_panel_login()

            elif entrypanel_selection =='3':
                panel.User_penel()

            elif entrypanel_selection == '4':
                print("Thank you for choosing us for your trip")
                exit()
            else:
                print("Your Entrance is wrong!\nPlease try again")
                panel.entry_panel()

    @staticmethod
    def admin_login_panel(username, password):
        input_user_name = input("Enter your username: ")
        while input_user_name != username:
            print('This username does not exists! please try again:')
            input_user_name = input('New username: ')
        input_password = input("Enter your passworrd: ")
        while input_password != password:
            print('This password is incorrect! please try again:')
            input_password = input('New password: ')
        print("Admin login successfully")
        panel.Admin_panel()
        
    @staticmethod
    def Admin_panel():     
        print("select a task")
        print("1-add train employee\n2-remove train employee\n3-view employees list\n4-exit from Admin panel")
        Admin_choice = input()
        if Admin_choice =='1':
            Admin.add_Employee()
        elif Admin_choice == '2':
            Admin.remove_Employee()
        elif Admin_choice == '3':
            Admin.Employee_list()
        elif Admin_choice == '4':
            panel.entry_panel()
        else:
            print("your choice is incorrect please try again")
            panel.Admin_panel()
                
    @staticmethod
    def employee_panel_login():
        while True:
            employee_username = input("Enter your username: ")
        
            if len(Admin.employee_list) == 0:
                print("There are no employees")
                panel.entry_panel()
            flag = False
            for k, v in Admin.employee_list.items():
                if employee_username == k:
                    flag = True
                    input_password = input("Enter your password: ")
                    if input_password == v.password:
                        print('Hi!')
                        print("Employee login successfuly")
                        panel.Employee_panel()
                        break
                    else:
                        print("Incorrect password. Please try again.")
            if not flag:
                print('This username does not exist! Please try again.')
                    
    
    def Employee_panel(): 
        print("select a task")
        print("1-add line\n2-update line\n3-remove line\n4-view line list\n5-add train\n6-remove train\n7-view train list\n8-exit from account")
        choice = input()
        if choice == '1': 
            Train_Employee.add_line()
        elif choice == '2': 
            Train_Employee.update_line()
        elif choice == '3': 
            Train_Employee.remove_line()
        elif choice == '4': 
            Train_Employee.display_lines()
        elif choice == '5': 
            Train_Employee.add_train()
        elif choice == '6': 
            Train_Employee.remove_train()
        elif choice == '7': 
            Train_Employee.train_list()
        elif choice == '8': 
            panel.entry_panel()

    @staticmethod
    def User_penel():
        print("1-Sign in\n2-log in\n3-back to first panel")
        user_selection = input()
        if user_selection == '1':
            User.add_user()
        elif user_selection == '2':
           User.login()
        elif user_selection== '3':
            panel.entry_panel()

    @staticmethod
    def purchase_panel():
        print("1-Buy ticket\n2-ِEdit profile\n3-wallet\n4-quit")
        select = input()
        if select == '1':
            if not Train_Employee.trains:
                print('no trains added yet')
                panel.purchase_panel()
            else:
                for v in Train_Employee.trains.values():
                    print(f'name: {v.train_name} , average_velocity: {v.average_velocity} , stops: {v.train_stop} , quality: {v.quality} , ticket_price: {v.ticket_price} , capacity: {v.capacity} , train_ID: {v.train_ID} , line: {v.train_line.name}')
                    
            selected_train=input("enter the trains id which you want to buy: ")
            for train in Train_Employee.trains.values():
                if train.train_ID == selected_train:
                    ticket_number=input("How many tickets do you want to buy?: ")
                    if int(train.capacity) >= int(ticket_number):
                        amount = int(v.ticket_price)*int(ticket_number)
                        if amount <= Wallet.balance :
                            train.capacity = int(train.capacity) - int(ticket_number)
                            Wallet.decrease(amount)
                            
                        else:
                            print("Not enough funds in the wallet.")
                            panel.purchase_panel()
                                      
                    else:
                        print('full') 
                        panel.purchase_panel()
                else:
                    print(f"{selected_train} does not exist!")
                    panel.purchase_panel()

        if select == '2':
            User.edit_user()
       
        if select == '3':
            selected_wallet=input('1-wallet information\n2-transfer money\n3-quit\n')
            if selected_wallet == '1':
                Wallet.info()

            elif selected_wallet == '2':
                amount = int(input("How much money do you want to add?: "))
                Wallet.increase(amount)
                
            elif selected_wallet=='3':
                panel.purchase_panel()

        if select == '4':
            panel.User_penel()

class Admin:

    employee_list = {}
    def add_Employee():
        name = input("Enter your name: ")
        while name == "":
            print("your input is empty")
            name = input("Please enter again:  ")
        
        last_name = input('Enter your last name: ')
        while last_name == "":
            print("your input is empty")
            last_name = input("Please enter again:  ")
        email = input('Enter your last Email: ')
        while email == "":
            print("your input is empty")
            email = input("Please enter again:  ")
        while email in Admin.employee_list:
            print('This email already exists! Choose another one:')
            email = input('Enter your email: ')
        username = input('Enter your username: ')
        while username in Admin.employee_list:
            print('This username already exists! Choose another one:')
            username = input('New username: ')
        while username == "":
            print("your input is empty")
            username = input("Please enter again:  ")
        password = input('Enter a password: ')
        while password == "":
            print("your input is empty")
            password = input("Please enter again:  ")
            
        Admin.employee_list[username] = Train_Employee(name, last_name, email, username, password)
        print(f"Employee {username} added successfully!")
        back = input("add another employee ""1"":\nreturn to Admin panel ""2"":\n")
        if back == '2':
            panel.Admin_panel()
        elif back == '1':
            Admin.add_Employee()
        else:
            print("this user name does not exist")
            Admin.add_Employee()
    
    def remove_Employee():
        user_name = input("Please Enter the username you want to remove: ")
        while user_name not in Admin.employee_list:
            print(f"Employee {user_name} does not exist in the system. Please provide a valid line name.")
            back = input("remove another employee ""1"":\nreturn to employee panel ""2"":\n")
            if back == '2':
                panel.Admin_panel()
            elif back == '1':
                user_name = input("Enter the name of the employyee you want to remove: ")
        key_list = list(Admin.employee_list.keys())
        for key in key_list:
            if key == user_name:
                del Admin.employee_list[key]
        print(f"{user_name} removed sucssesfully")
        back_1 = input("remove another employee ""1"":\nreturn to Admin panel ""2"":\n")
        if back_1 == '2':
            panel.Admin_panel()
        elif back_1 == '1':
            Admin.remove_Employee()
            

    def Employee_list():
        if not Admin.employee_list:
            print('no Employee added yet')
            panel.Admin_panel
        else:
            for v in Admin.employee_list.values():
                print(f'name: {v.name}')
                print(f'last name: {v.last_name}')
                print(f'Email: {v.email}')
                print(f'username: {v.username}')
                print(f'password: {v.password}')
            back = input("return to Admin panel ""1"":\n")
            if back == '1':
                panel.Admin_panel()

class Wallet:

    balance = 0
    def __init__(self, cardnumber, password):
        self.cardnumber = cardnumber
        self.password = password
    
    @classmethod
    def info(cls):
        print(f" balance: {cls.balance}")
        panel.purchase_panel()

    @classmethod
    def increase(cls, amount):
        cls.balance += amount
        print(f" balance: {cls.balance}")
        panel.purchase_panel()

    @classmethod
    def decrease(cls, amount):
        if amount <= cls.balance:
                cls.balance -= amount
                print("have a nice trip")
                panel.purchase_panel()
        

class Train:
    
    def __init__(self, train_name, average_velocity, train_stop, quality, ticket_price, capacity, train_ID ,train_line):
        self.train_name = train_name
        self.train_line = train_line
        self.average_velocity = average_velocity
        self.train_stop = train_stop
        self.quality = quality
        self.ticket_price = ticket_price
        self.capacity = capacity
        self.train_ID = train_ID
        

class Train_Employee:

    trains= {} 
    lines = {}
    def __init__(self, name, last_name, email, username, password, **kwargs):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.last_name = last_name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    @classmethod
    def add_line(cls):
            name = input("please enter the line name:  ")
            while name == "":
                print("your input is empty")
                name = input("Please enter again:  ")
            origin = input("please enter the origin:  ")
            while origin == "":
                print("your input is empty")
                origin = input("Please enter again:  ")
            destination = input("please enter the destination:  ")
            while destination == "":
                print("your input is empty")
                destination = input("Please enter again:  ")
                
            while origin == destination:
                print("The origin is the same as the destination.")
                origin = input("please enter the origin: ")
                destination = input("please enter the destination: ")
                if origin != destination:
                    break
            number_of_stations = input("How many stations do you want to add?: ")
            while number_of_stations == "":
                print("your input is empty")
                number_of_stations = input("Please enter again:  ")
            
            while not number_of_stations.isdigit():
                print("The number of stations must be a number")
                number_of_stations = input("How many stations do you want to add?: ")
            
            count = 0
            stationlist = []
            while count <  int(number_of_stations):
                station = input("Enter station name: ")
                if station in stationlist:
                    print("Station name already exists. Please enter a different station name.")
                else:
                    stationlist.append(station)  
                    count += 1
            if name not in cls.lines:
                cls.lines[name] = Line(name , origin , destination , stationlist ,number_of_stations)
                print(f"Line {name} added successfully!")
                back = input("add another line ""1"":\nreturn to employee panel ""2"":\n")
                if back == '2':
                    panel.Employee_panel()
                elif back == '1':
                    Train_Employee.add_line()
            else:
                print(f"Line {name} already exists! Please choose a different name for the line.")
                back = input("add another line ""1"":\nreturn to employee panel ""2"":\n")
                if back == '2':
                    panel.Employee_panel()
                elif back == '1':
                    Train_Employee.add_line()

    @classmethod
    def update_line (cls):
        line_name = input("Enter the name of the line you want to update: ")
        while line_name not in cls.lines:
                print(f"Line {line_name} does not exist.")
                line_name = input("Enter the name of the line you want to update: ")
                if line_name in cls.lines:
                    break

        for key, value in cls.lines.items():
            if key == line_name:
                i = input("Which attribute would you like to update? (name, origin, destination or station): ")
                if i == "origin":
                    new_origin = input("Enter the new origin: ")
                    while new_origin == "":
                            print("your input is empty")
                            new_origin = input("Please enter again:  ")
                    cls.lines[line_name].origin = new_origin
                    print("origin updated successfully!")
                    back = input("update another line ""1"":\nreturn to employee panel ""2"":\n")
                    if back == '2':
                        panel.Employee_panel()
                    elif back == '1':
                        Train_Employee.update_line()

                elif i == "destination":    
                    new_destination = input("Enter the new destination: ")
                    while new_destination == "":
                            print("your input is empty")
                            new_destination = input("Please enter again:  ")
                    cls.lines[line_name].destination = new_destination
                    print("destination updated successfully!")
                    back = input("update another line ""1"":\nreturn to employee panel ""2"":\n")
                    if back == '2':
                        panel.Employee_panel()
                    elif back == '1':
                        Train_Employee.update_line()

                elif i == "name":    
                    new_name = input("Enter the new name: ")
                    while new_name == "":
                            print("your input is empty")
                            new_name = input("Please enter again:  ")
                    cls.lines[line_name].name = new_name
                    cls.lines[new_name] = cls.lines[line_name]
                    del cls.lines[line_name]
                    print("name updated successfully!")
                    back = input(" update another line ""1"":\nreturn to employee panel ""2"":\n")
                    if back == '2':
                        panel.Employee_panel()
                    elif back == '1':
                        Train_Employee.update_line()
            
                elif i == "station":
                    station_input = input('1-change  2-add  3-reset and add new stations:\n')
                    if station_input == '1':
                        old_station = input("Enter the station you want to change: ")
                        new_station = input("Enter the new station name: ")
                        while new_station == "":
                            print("your input is empty")
                            new_station = input("Please enter again:  ")
                        if old_station in value.stations:
                            index = value.stations.index(old_station)
                            value.stations[index] = new_station
                            print("Stations updated successfully!")
                            print("Stations updated successfully!")
                            back = input("update another line ""1"":\nreturn to employee panel ""2"":\n")
                            if back == '2':
                                panel.Employee_panel()
                            elif back == '1':
                                Train_Employee.update_line()
                        else:
                            print(f"Station {old_station} does not exist.")
                            Train_Employee.update_line()
                    elif station_input == '2':
                        number_of_stations = input("How many stations do you want to add?: ")
                        while not number_of_stations.isdigit():
                            print("The number of stations must be a number")
                            number_of_stations = input("How many stations do you want to add?: ")
                        count = 0
                        while count < int(number_of_stations):
                            station = input("Enter station name: ")
                            if station in value.stations:
                                print("Station name already exists. Please enter a different station name.")
                            else:
                                value.stations.append(station)  
                                count += 1
                        stationlist_number += number_of_stations
                        print("Stations updated successfully!")
                        back = input("update another line ""1"":\nreturn to employee panel ""2"":\n")
                        if back == '2':
                            panel.Employee_panel()
                        elif back == '1':
                            Train_Employee.update_line()
                        
                    elif station_input == '3':
                        value.stations.clear()
                        number_of_stations = int(input("How many stations do you want to add?: "))
                        count = 0
                        while count < number_of_stations:
                            station = input("Enter station name: ")
                            value.stations.append(station)  
                            count += 1
                        stationlist_number = number_of_stations
                        print("Stations updated successfully!")
                        back = input("update another line ""1"":\nreturn to employee panel ""2"":\n")
                        if back == '2':
                            panel.Employee_panel()
                        elif back == '1':
                            Train_Employee.update_line()
                else:
                    print("Invalid attribute choice. Please choose 'name', 'origin', 'destination', or 'station'.")
                    Train_Employee.update_line

    @classmethod      
    def remove_line(cls):
        if not cls.lines:
            print("No lines added yet.")
            panel.Employee_panel()
        else:
            line_name = input("Enter the name of the line you want to remove: ")
            while line_name not in cls.lines:
                print(f"Line {line_name} does not exist in the system. Please provide a valid line name.")
                line_name = input("Enter the name of the line you want to remove: ")
            
            if line_name in cls.lines:
                del cls.lines[line_name]
                key_list = list(cls.trains.keys())
                for key in key_list:
                    if cls.trains[key].train_line.name == line_name:
                        del cls.trains[key]
                print(f"Line {line_name} removed successfully!")
                back = input("remove another line ""1"":\nreturn to employee panel ""2"":\n")
                if back == '2':
                    panel.Employee_panel()
                elif back == '1':
                    Train_Employee.remove_line()

    @classmethod
    def display_lines(cls):      
        if not cls.lines:
            print("No lines added yet.")
            panel.Employee_panel()
        else:
            print("List of added lines:")
            for key , value in cls.lines.items():
                number = len(value.stations)
                print(f"Line name: {value.name}")
                print(f"origin: {value.origin}")
                print(f"destination: {value.destination}")
                print("Stations:")
                for station in value.stations:
                    print(f"  - {station}")
                print(f'number of stations:  {number}')
            back = input("return to employee panel ""1"":\n")
            if back == '1':
                panel.Employee_panel()

    @classmethod
    def add_train(cls):
        name = input("Please enter the train name: ")
        while name == "":
            print("your input is empty")
            name = input("Please enter again:  ")
        average_velocity = input("Please enter the average velocity: ")
        while average_velocity == "":
            print("your input is empty")
            average_velocity = input("Please enter again:  ")
            
        while not average_velocity.isdigit():
                print("The average velocity must be a number")
                average_velocity = input("Please enter the average velocity: ")
                
        stops = input("Please enter the duration of the train stop: ")
        while not stops.isdigit():
                print("The stops must be a number")
                stops = input("Please enter the duration of the train stop: ")
        while stops == "":
            print("your input is empty")
            stops = input("Please enter again:  ")
            
                
        quality = int(input("Please enter the quality from 1 to 5: "))
        while quality>5 or quality<1 or quality=="":
            print("The number must be between one and five")
            quality = int(input("Please enter the quality from 1 to 5: "))
        ticket_price = input("Please enter the ticket price: ")
        while not ticket_price.isdigit():
                print("The ticket price must be a number")
                ticket_price = input("Please enter the ticket price: ")
        while ticket_price == "":
            print("your input is empty")
            ticket_price = input("Please enter again:  ")
            
        capacity = input("Please enter the capacity: ")
        while not capacity.isdigit():
            print("The capacity must be a number")
            capacity = input("Please enter the capacity: ")
            
        while capacity == "":
            print("your input is empty")
            capacity = input("Please enter again:  ")

        train_ID = input("Please enter the train id: ")
        while train_ID == "":
            print("your input is empty")
            train_ID = input("Please enter again:  ")

        
        line_name = input("Please enter the line: ")
        while line_name == "":
            print("your input is empty")
            line_name = input("Please enter again:  ")
                
        if line_name in cls.lines:
            if train_ID not in cls.trains:
                cls.trains[train_ID] = Train(name, average_velocity, stops, quality, ticket_price, capacity, train_ID, cls.lines[line_name])
                print(f"Train {train_ID} added successfully!")
                back = input("add another train ""1"":\nreturn to employee panel ""2"":\n")
                if back == '2':
                    panel.Employee_panel()
                elif back == '1':
                    Train_Employee.add_train()
            elif train_ID in cls.trains:
                print("This is a duplicate train id.")
                Train_Employee.add_train()
            else:
                print(f"Train {train_ID} already exists! Please choose a different name for the train.")
                Train_Employee.add_train()
        else:
            print(f"Line {line_name} does not exist! Please enter a valid line.")
            Train_Employee.add_train()

    @classmethod
    def remove_train(cls):
        train_ID =input("which train you want to remove?: ")
        if train_ID  in cls.trains:
            del cls.trains[train_ID]
            print(f"train {train_ID} removed successfully!")
            back = input("ramove another train ""1"":\nreturn to employee panel ""2"":\n")
            if back == '2':
                panel.Employee_panel()
            elif back == '1':
                Train_Employee.remove_line()
        else:
            print(f"train {train_ID} does not exist in the system. Please provide a valid train id.")
            back = input("ramove another train ""1"":\nreturn to employee panel ""2"":\n")
            if back == '2':
                panel.Employee_panel()
            elif back == '1':
                Train_Employee.remove_line()

    @classmethod        
    def train_list(cls):
        if not cls.trains:
            print('no trains added yet')
            panel.Employee_panel()
        else:
            for v in cls.trains.values():
                print(f'name: {v.train_name}')
                print(f'average_velocity: {v.average_velocity}')
                print(f'stops: {v.train_stop}')
                print(f'quality: {v.quality}')
                print(f'ticket_price: {v.ticket_price}')
                print(f'capacity: {v.capacity}')
                print(f'train_id: {v.train_ID}')
                print(f'line: {v.train_line.name}')
                back = input("return to employee panel ""1"":\n")
                if back == '1':
                    panel.Employee_panel()

class Line:
   
    def __init__(self, name, origin, destination, stations:list , stations_number):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.stations = stations
        self.stations_number = stations_number


class User:
    users = {}  
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def add_user(cls):
        name = input("Enter your name: ")
        while name == "":
            print("your input is empty")
            name = input("Please enter again:  ")
        
        email = input('Enter your email: ')
        while email == "":
            print("your input is empty")
            email = input("Please enter again:  ")
        
        while email in cls.users:
            print('This email already exists! Choose another one:')
            email = input('Enter your email: ')
        username = input('Enter a username: ')
        while username in cls.users:
            print('This username already exists! Choose another one:')
            username = input('New username: ')
        password = input('Enter a password: ')
        cls.users[username] = User(name, email, username, password)
        print("Sign in sucssesfully")
        back = input("return to User panel ""1"":\n")
        if back == '1':
            panel.User_penel()


    @classmethod
    def login(cls):
        if not cls.users:
            print("Please Sign in first.")
            panel.User_penel()
        else:
            username = input('Please enter your username: ')
            while username not in cls.users:
                print('This username does not exist. Try again!')
                username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            while cls.users[username].password != password:
                print('This password does not match with your username. Try again!!')
                password = input('Enter your password: ')
            print('Welcome!')
            panel.purchase_panel()

    @classmethod
    def edit_user(cls):
        username = input("Enter your username: ")
        while username not in cls.users:
                print(f"your username is wrong.")
                username = input("Enter your username: ")
                if username in cls.users:
                    break
        
        for key, value in cls.users.items():
            if key == username:          
                edit=input('Which attribute would you like to edit ?(name,email,username,password):  ')
                
                if edit=='name':
                    new_name = input("Please enter a new name:  ")
                    while new_name == "":
                        print("your input is empty")
                        new_name = input("Please enter a new name:  ")
                    
                    cls.users[username].name = new_name
                    print("name edited successfully!")
                    panel.purchase_panel()

                elif edit=='email':
                    new_email = input('Enter a  new email: ')
                    while new_email == "":
                        print("your input is empty")
                        new_email = input("Please enter a new email:  ")
                    for v in cls.users.values():
                        while new_email == v.email:
                            print('This email already exists!')
                            back = input("Enter a new email ""1"":\nreturn to purchase panel ""2"":\n")
                            if back == '2':
                                panel.purchase_panel()
                            elif back == '1':
                                new_email = input('New email: ')
                                while new_email == "":
                                    print("your input is empty")
                                    new_email = input("Please enter a new email:  ")
                        cls.users[username].email = new_email
                        print("email edited successfully!")
                        panel.purchase_panel()

                elif edit=='username':
                    new_username = input('Enter a username: ')
                    while new_username == "":
                        print("your input is empty")
                        new_username = input("Please enter a new username:  ")
                        
                    while new_username in cls.users:
                        print('This username  already exists!')
                        back = input("Enter a new username ""1"":\nreturn to purchase panel ""2"":\n")
                        if back == '2':
                            panel.purchase_panel()
                        elif back == '1':
                            new_username = input('New username: ')
                            while new_username == "":
                                print("your input is empty")
                                new_username = input("Please enter a new username:  ")
                            
                    cls.users[username].username = new_username
                    print("username edited successfully!")
                    cls.users[new_username] = cls.users[username]
                    del cls.users[username]
                    panel.purchase_panel()
                
                elif edit=='password':
                    new_password = input("Please enter a new password:  ")
                    while new_password == "" :
                        print("your input is empty")
                        new_password = input("Please enter a new password:  ")
                    cls.users[username].password = new_password
                    print("password edited successfully!")
                    panel.purchase_panel()

a = panel()
a.entry_panel()