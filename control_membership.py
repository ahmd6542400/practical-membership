admins = ['Ahmed' , 'Ali' , 'Mohamed' , 'Karem' , 'Ramy']
name = input('please enter Ur name: ').strip().capitalize()

if name in admins:
    print(f'Hello {name} Welcome Back')
    option = input('delete or update your name: ').strip().capitalize()
    
    if  option == 'Update' or option == 'U':
        new_name = input('enter new name: ').strip().capitalize()
        admins[admins.index(name)] = new_name
        print('name updated')
        print(admins)

    elif option == 'Delete' or option == 'D':
        admins.remove(name)
        print('name deleted')
        print(admins)

    else:
        print('woring option choosed')    

else:
    status = input('not admin, ADD U: ').strip().capitalize()

    if status == 'Yes' or status == 'Y':
        admins.append(name)
        print('U have been added')
        print(admins)

    else:
        print("U are not added")    
