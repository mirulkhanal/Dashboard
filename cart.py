item_list = ['apple', 'banana', 'mango']


def take_user_input():
    global item_list
    while True:
        query = input('\n 1) Add an Item  \n 2) Remove an Item \n 3) Quit \n')
        if query == '1':
            item = input("Enter the item you want to add: ")
            item_list.append(item)
            print(item_list)
        elif query == '2':
            try:
                item = input('Enter item to remove ')
                item_list.remove(item)
            except ValueError as error:
                print('Item not found')
        elif query == '3':
            print('Program exited with code 0')
            break
        else:
            print('Invalid option, Please Try again')


print(item_list)
take_user_input()
