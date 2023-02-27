# ----------------------------------------------
# Author: Mohamad Boukaili
# Date: Fall 2022
# Course: Principles of programming languages
# Title: Small database server with Python
# ----------------------------------------------
# Server side
# ----------------------------------------------
import socket
import sys

# ----------------------------------------------
# SERVER FUNCTIONS      
# ----------------------------------------------

# Load databse as a list of tuples

def database_load():
    global database_list
    database_list = []
    global tuples_count
    tuples_count = 0
    with open("data.txt", "r") as file:
        for line in file:
            info_list = []
            for word in line.split("|"):
                info_list.append(word.strip())
            # If name is not empty then perform, else don't
            if info_list[0] != "":
                info_tuple = tuple(info_list)
                database_list.append(info_tuple)
    
# find customer by name function
def find_customer(first_name, database_list):
    counter = 0
    for x in database_list:
        if first_name.strip() == x[0]:
            print(x[0], "found and info sent to client.")
            client_socket.send(("Server response: " + x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3]).encode("utf-8"))
            break
        #if customer name not found, increment count and iterate.
        #when the count is equal to the length of the database list
        #that means the customer wasn't found.
        else:
            counter += 1
            if counter is (len(database_list)):
                print(first_name.strip(), " not found.")
                client_socket.send(bytes("Server response: Customer not found in Database. ", "utf-8"))
                break

#boolean customer already exists
def customer_already_exists(first_name, age, address, phone_number):
    for x in database_list:
        if first_name.strip() in x and age.strip() in x and address.strip() in x and phone_number.strip() in x:
            return True

#add customer function
def add_customer(first_name, age, address, phone_number):
    if customer_already_exists(first_name, age, address, phone_number) is True:
            print("Couldn't add new customer because they already exist.")
            client_socket.send(bytes("\nServer response: Customer already exists.", "utf-8"))
            return
    else: 
        info_tuple = (first_name.strip(), age.strip(), address.strip(), phone_number.strip())
        database_list.append(info_tuple)

        print(first_name, "|", age, "|", address, "|", phone_number, ": has been added successfully to the database.", sep="")
        client_socket.send(bytes("\nServer response: Customer added succesfully.", "utf-8"))
        return

#remove tuple off the list
def remove_element_that_contains(first_name, age, address, phone_number):
    for x in database_list:
        if first_name.strip() in x and age.strip() in x and address.strip() in x and phone_number.strip() in x:
            database_list.remove((first_name.strip(), age.strip(), address.strip(), phone_number.strip()))
            break

#delete customer function
def delete_customer(first_name, age, address, phone_number):
    if customer_already_exists(first_name, age, address, phone_number) is not True:
        print("\nCustomer does not exist.")
        client_socket.send(bytes("\nServer response: Customer does not exist.", "utf-8"))
        return
    else: 
        remove_element_that_contains(first_name, age, address, phone_number)

        print(first_name, "|", age, "|", address, "|", phone_number, ": has been deleted successfully from the database.", sep="")
        client_socket.send(bytes("\nServer response: Customer deleted succesfully.", "utf-8"))
        return

#update age
def update_customer_age(first_name, age):
    counter = 0
    for x in database_list:
        #if found, modify
        if first_name.strip() in x:
            info_tuple = (x[0], age, x[2], x[3])
            database_list[counter] = (info_tuple)

            print(first_name, "\'s age has been succesfully updated to ", age, ".", sep="")
            client_socket.send(bytes("\nServer response: Customer age updated succesfully.", "utf-8"))
            break
        #if customer name not found, increment count and iterate.
        #when the count is equal to the length of the database list
        #that means the customer wasn't found.
        elif first_name.strip() not in x:
            counter += 1
            if counter is (len(database_list)):
                print(first_name.strip(), "not found.")
                client_socket.send(bytes("\nServer response: Customer not found.", "utf-8"))
                break
        
#update address
def update_customer_address(first_name, address):
    counter = 0
    for x in database_list:
        #if found, modify
        if first_name.strip() in x:
            info_tuple = (x[0], x[1], address, x[3])
            database_list[counter] = (info_tuple)

            print(first_name, "\'s address has been succesfully updated to ", address, ".", sep="")
            client_socket.send(bytes("\nServer response: Customer address updated succesfully.", "utf-8"))
            break
        #if customer name not found, increment count and iterate.
        #when the count is equal to the length of the database list
        #that means the customer wasn't found.
        elif first_name.strip() not in x:
            counter += 1
            if counter is (len(database_list)):
                print(first_name.strip(), "not found.")
                client_socket.send(bytes("\nServer response: Customer not found.", "utf-8"))
                break
            
#update phone number
def update_customer_phone_number(first_name, phone_number):
    counter = 0
    for x in database_list:
        if first_name.strip() in x:
            info_tuple = (x[0], x[1], x[2], phone_number)

            database_list[counter] = (info_tuple)
            print(first_name, "\'s phone number has been succesfully updated to ", phone_number, ".", sep="")
            client_socket.send(bytes("\nServer response: Customer phone number updated succesfully.", "utf-8"))
            break
        #if customer name not found, increment count and iterate.
        #when the count is equal to the length of the database list
        #that means the customer wasn't found.
        elif first_name.strip() not in x:
            counter += 1
            if counter is (len(database_list)):
                print(first_name.strip(), "not found.")
                client_socket.send(bytes("\nServer response: Customer not found.", "utf-8"))
                break

#print report
def print_report():
    python_db_contents = ""
    for x in database_list:
        python_db_contents += x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3] + "\n"
    print("DB content sent to client.")
    db_contents = "\nServer response:\n\n** Python DB contents **\n\n" + python_db_contents
    client_socket.send(bytes(db_contents, "utf-8"))
    
# ----------------------------------------------
# SERVER FUNCTIONS END
# ----------------------------------------------

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    
    request_number = 0
    #load data
    database_load()

    sock = socket.socket()
    sock.bind(("localhost", 9999))
    print("Server started on port= ", PORT)
    sock.listen(5)
    client_socket, client_address = sock.accept()
    print("Client connected with address: ", client_address[0]) 
    
    while True:
        #recieve input from client and print request on the server's terminal
        select_option = client_socket.recv(1024).decode()
        print(request_number, ". Client selected option: ", select_option, sep="")
        # Exit
        if int(select_option.strip()) == 8:
                print("Client exited with option 8.")
                client_socket.close()
                sys.exit()
        #The input variable evaluation is done on the client's side.
        #Once they're evaluated (example: Check_name_format), the server recieves 
        #the the correct format of the input variable and decides which function
        #to call depending on the select_option input variable and in respect
        #with the other input variables as well (number name address etc).
        #The server terminal will output: the request number, the option selected by the client, 
        #and the result of the operation (succesful vs unsuccesful operation)
        else:
                # 1. Find customer
                if int(select_option.strip()) == 1:
                    first_name = client_socket.recv(1024).decode()
                    find_customer(first_name, database_list)
                
                # 2. Add customer
                elif int(select_option.strip()) == 2:
                    first_name = client_socket.recv(1024).decode()
                    age = client_socket.recv(1024).decode()
                    address = client_socket.recv(1024).decode()
                    phone_number = client_socket.recv(1024).decode()
                    add_customer(first_name, age, address, phone_number)
                    
                # 3. Delete customer
                elif int(select_option.strip()) == 3:
                    first_name = client_socket.recv(1024).decode()
                    age = client_socket.recv(1024).decode()
                    address = client_socket.recv(1024).decode()
                    phone_number = client_socket.recv(1024).decode()
                    delete_customer(first_name, age, address, phone_number)
                    
                # 4. Update customer age
                elif int(select_option.strip()) == 4:
                    first_name = client_socket.recv(1024).decode()
                    age = client_socket.recv(1024).decode()
                    update_customer_age(first_name, age)
        
                # 5. Update customer address
                elif int(select_option.strip()) == 5:
                    first_name = client_socket.recv(1024).decode()
                    address = client_socket.recv(1024).decode()
                    update_customer_address(first_name, address)
                
                # 6. Update customer phone number
                elif int(select_option.strip()) == 6:
                    first_name = client_socket.recv(1024).decode()
                    phone_number = client_socket.recv(1024).decode()
                    update_customer_phone_number(first_name, phone_number)
                    
                # 7. Print report
                elif int(select_option.strip()) == 7:
                    print_report()

        request_number += 1
    