# ----------------------------------------------
# Author: Mohamad Boukaili
# Date: Fall 2022
# Course: Principles of programming languages
# Title: Small database server with Python
# ----------------------------------------------
# Client side
# ----------------------------------------------
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
listOfGlobals = globals()

#print menu function
def print_menu():
    print (""" 
Python DB Menu    
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address 
6. Update customer phone number
7. Print report
8. Exit 
""")

#check select option input format
def check_selectoption_format(select_option):
    if select_option.strip() == "" or not select_option.isdigit() or int(select_option.strip()) > 8 or int(select_option.strip()) <= 0:
        send_data = False
        while not send_data:
            select_option = input("Please enter a valid option: ")
            if select_option.strip() != "" and select_option.isdigit() and int(select_option.strip()) <= 8 and int(select_option.strip()) > 0:
                #update input value globally
                listOfGlobals["select_option"] = select_option
                send_data = True
                return True
    else: return True

#check name input format
def check_name_format(first_name):
    if first_name.strip() == "" or first_name.isdigit():
        send_data = False
        while not send_data:
            first_name = input("Please enter a valid name: ")
            if first_name.strip() != "" and not first_name.isdigit():
                #update input value globally
                listOfGlobals["first_name"] = first_name
                send_data = True
                return True
    else: return True

#check age input format
def check_age_format(age):
    if age.strip() == "":
        return True
    elif not age.isdigit():
        send_data = False
        while not send_data:
            age = input("Please enter a valid age: ")
            if age.isdigit():
                send_data = True
                #update input value globally
                listOfGlobals["age"] = age
                return True
    else: return True

# Create a socket (SOCK_STREAM means a TCP socket)
if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        
        print_menu()
        select_option = input("Select Option: ")

        # Check if input is valid
        while not check_selectoption_format(select_option):
            select_option = input("Please enter a valid option: ")

        while int(select_option.strip()):
            sock.send(bytes(select_option, "utf-8"))
            # Exit
            if int(select_option.strip()) == 8:
                # client_socket.send(bytes("Program terminated. Good bye!", "utf-8"))
                print("\nProgram terminated. Goodbye!")
                sys.exit()
            else:
                # 1. Find customer
                if int(select_option.strip()) == 1:
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))

                    # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue

                # 2. Add customer
                elif int(select_option.strip()) == 2:
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))

                    age = input("Customer Age: ")
                    # Check if age format is correct, when true send data
                    if check_age_format(age):
                        #Send "space" rather than "null", otherwise the server won't
                        #recieve anything and the program will get stuck
                        if age.strip() == "": 
                            sock.send(bytes(" ", "utf-8"))
                        else: sock.send(bytes(age, "utf-8"))

                    address = input("Customer Address: ")
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if address.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    else: sock.send(bytes(address, "utf-8"))

                    phone_number = input("Customer Phone Number: ")
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if phone_number.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    sock.send(bytes(phone_number, "utf-8"))
                
                    # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue
                    

                # 3. Delete customer
                elif int(select_option.strip()) == 3:
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))

                    age = input("Customer Age: ")
                    # Check if age format is correct, when true send data
                    if check_age_format(age):
                        #Send "space" rather than "null", otherwise the server won't
                        #recieve anything and the program will get stuck
                        if age.strip() == "": 
                            sock.send(bytes(" ", "utf-8"))
                        else: sock.send(bytes(age, "utf-8"))

                    address = input("Customer Address: ")
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if address.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    else: sock.send(bytes(address, "utf-8"))

                    phone_number = input("Customer Phone Number: ")
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if phone_number.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    sock.send(bytes(phone_number, "utf-8"))
                    
                    # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue
                    
                
                # 4. Update customer age
                elif int(select_option.strip()) == 4:
                    
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))
        
                    age = input("Customer Age: ")       
                    # Check if age format is correct, when true send data
                    if check_age_format(age):
                        #Send "space" rather than "null", otherwise the server won't
                        #recieve anything and the program will get stuck
                        if age.strip() == "": 
                            sock.send(bytes(" ", "utf-8"))
                        else: sock.send(bytes(age, "utf-8"))
                    
                    # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue
                    

                # 5. Update customer address
                elif int(select_option.strip()) == 5:
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))

                    address = input("Customer Address: ")
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if address.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    else: sock.send(bytes(address, "utf-8"))
                    
                    # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue
                    

                # 6. Update customer phone number
                elif int(select_option.strip()) == 6:
                    first_name = input("\nCustomer Name: ")
                    # Check if name format is correct, when true send data
                    if check_name_format(first_name):
                        sock.send(bytes(first_name, "utf-8"))
                    
                    #Send "space" rather than "null", otherwise the server won't
                    #recieve anything and the program will get stuck
                    if phone_number.strip() == "":
                        sock.send(bytes(" ", "utf-8"))
                    sock.send(bytes(phone_number, "utf-8"))

                   # recieve result from server
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))
                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue
                    
                
                # 7. Print report
                elif int(select_option.strip()) == 7:
                                
                    receive = str(sock.recv(1024), "utf-8")
                    print("{}".format(receive))

                    print_menu()
                    select_option = input("Select Option: ")
                    if check_selectoption_format(select_option):
                        continue

                    
