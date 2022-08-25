from views import *

print('What do you want be? CREATE, LISTING, RETRIEVE, UPDATE, DELETED, EXIT')

while True:
    operation = input('Enter action: ')
    if operation == "LISTING":
        print(listing())
    elif operation == "RETRIEVE":
        print(retrieve())
    elif operation == "CREATE":
        print(create())
    elif operation == "UPDATE":
        print(update())
    elif operation == 'DELETED':
        print(delete_data())
    elif operation == "EXIT":
        break
    else:
        print("Erroe write!!!")