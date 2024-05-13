import easygui as gui
import os
import time

def main():
    choice = gui.choicebox(
        msg='Welcome to the ACM user management system! Please select an option below:',
        title='ACM',
        choices=['Create/Delete User', 'Enable/Disable User', 'Change Privileges', 'Change Password', 'List Users', 'Exit'],
    )

    if choice == 'Create/Delete User':
        createdeleteuser()

    elif choice == 'Enable/Disable User':
        enabledisableuser()

    elif choice == 'Change Privileges':
        changeprivileges()

    elif choice == 'Change Password':
        changepassword()

    elif choice == 'List Users':
        listusers()

    elif choice == 'Exit':
        gui.msgbox(
            msg='Thank you for using ACM!',
            title='Thank you!',
            ok_button='Exit'
        )
        exit()

    else:
        gui.msgbox(
            msg='Thank you for using ACM!',
            title='Thank you!',
            ok_button='Exit'
        )

def createdeleteuser():
        choice = gui.choicebox(
            msg='Are you Creating or Deleting a user?',
            title='Create/Delete User',
            choices=['Creating', 'Deleting', 'Back']
        )

        if choice == 'Creating':
            creating()

        elif choice == 'Deleting':
            deleting()

        elif choice == 'Back':
            main()

def creating():
    username = gui.textbox(
        msg="What's the username?",
        title='Create User',
    )

    if username is None:
        gui.buttonbox(
            msg='User creation cancelled!',
            title='Create User',
            choices=['Back']
        )
        main()
        return

    password = gui.textbox(
        msg="What's the password?",
        title='Create User',
    )

    if password is None:
        gui.buttonbox(
            msg='User creation cancelled!',
            title='Create User',
            choices=['Back']
        )
        main()
        return

    admin = gui.boolbox(
        msg='Will this user be an admin?',
        title='Create User',
        choices=['Yes', 'No']
    )

    if admin is None:
        gui.buttonbox(
            msg='User creation cancelled!',
            title='Create User',
            choices=['Back']
        )
        main()
        return

    enabled = gui.boolbox(
        msg='Will this user be enabled?',
        title='Create User',
        choices=['Yes', 'No']
    )

    if enabled is None:
        gui.buttonbox(
            msg='User creation cancelled!',
            title='Create User',
            choices=['Back']
        )
        main()
        return

    confirm = gui.boolbox(
        msg='Are you sure you want to make user ' + username + ' with password ' + password + ' ?',
        title='Create User',
        choices=['Yes', 'No']
    )

    if confirm == True:
        os.system('net user ' + username + ' ' + password + ' /add')

        if admin == True:
            os.system('net localgroup Administrators ' + username + ' /add')

        if enabled == False:
            os.system('net user ' + username + ' /active:no')

        gui.buttonbox(
            msg='User created successfully!',
            title='Create User',
            choices=['Back']
            )
        main()

    else:
        gui.buttonbox(
            msg='User creation cancelled!',
            title='Create User',
            choices=['Back']
            ) 
        main()

def deleting():
    allaccounts = os.popen('net user').read()
    account = gui.textbox(
        msg="Select an account to delete: \n \n" + allaccounts,
        title='Delete User',
    )

    confirmation = gui.boolbox(
        msg='Are you sure you want to delete ' + account + '?',
        title='Delete User',
        choices=['Yes', 'No']
    )
    
    if confirmation == True:
        os.system('net user ' + account + ' /delete')
        gui.buttonbox(
            msg='User deleted successfully!',
            title='Delete User',
            choices=['Back']
        )
        main()

    else:
        gui.buttonbox(
            msg='User deletion cancelled!',
            title='Delete User',
            choices=['Back']
        )
        main()

def listusers():
    accounts = os.popen('net user').read()
    gui.buttonbox(
        msg=accounts,
        title='List Users',
        choices=['Back']
    )
    main()

def enabledisableuser():
    choice = gui.choicebox(
        msg='Are you Enabling or Disabling a user?',
        title='Enable/Disable User',
        choices=['Enabling', 'Disabling', 'Back']
    )

    if choice == 'Enabling':
        enabling()

    elif choice == 'Disabling':
        disabling()

    elif choice == 'Back':
        main()

def enabling():
    allaccounts = os.popen('net user').read()
    account = gui.textbox(
        msg="Select an account to enable: \n \n" + allaccounts,
        title='Enable User',
    )

    confirmation = gui.boolbox(
        msg='Are you sure you want to enable ' + account + '?',
        title='Enable User',
        choices=['Yes', 'No']
    )
    
    if confirmation == True:
        os.system('net user ' + account + ' /active:yes')
        gui.buttonbox(
            msg='User enabled successfully!',
            title='Enable User',
            choices=['Back']
        )
        main()

    else:
        gui.buttonbox(
            msg='User enabling cancelled!',
            title='Enable User',
            choices=['Back']
        )
        main()

def disabling():
    allaccounts = os.popen('net user').read()
    account = gui.textbox(
        msg="Select an account to disable: \n \n" + allaccounts,
        title='Disable User',
    )

    confirmation = gui.boolbox(
        msg='Are you sure you want to disable ' + account + '?',
        title='Disable User',
        choices=['Yes', 'No']
    )
    
    if confirmation == True:
        os.system('net user ' + account + ' /active:no')
        gui.buttonbox(
            msg='User disabled successfully!',
            title='Disable User',
            choices=['Back']
        )
        main()

    else:
        gui.buttonbox(
            msg='User disabling cancelled!',
            title='Disable User',
            choices=['Back']
        )
        main()

def changeprivileges():
    allaccounts = os.popen('net user').read()
    account = gui.textbox(
        msg="Select an account to change privileges: \n \n" + allaccounts,
        title='Change Privileges',
    )

    admin = gui.boolbox(
        msg='Will this user be an admin?',
        title='Change Privileges',
        choices=['Yes', 'No']
    )

    if admin is None:
        gui.buttonbox(
            msg='Privilege change cancelled!',
            title='Change Privileges',
            choices=['Back']
        )
        main()
        return

    if admin == True:
        os.system('net localgroup Administrators ' + account + ' /add')

    else:
        os.system('net localgroup Administrators ' + account + ' /delete')

    gui.buttonbox(
        msg='Privileges changed successfully!',
        title='Change Privileges',
        choices=['Back']
    )
    main()

def changepassword():
    allaccounts = os.popen('net user').read()
    account = gui.textbox(
        msg="Select an account to change password: \n \n" + allaccounts,
        title='Change Password',
    )

    password = gui.textbox(
        msg="What's the new password?",
        title='Change Password',
    )

    if password is None:
        gui.buttonbox(
            msg='Password change cancelled!',
            title='Change Password',
            choices=['Back']
        )
        main()
        return

    confirm = gui.boolbox(
        msg='Are you sure you want to change the password for ' + account + ' to ' + password + '?',
        title='Change Password',
        choices=['Yes', 'No']
    )

    if confirm == True:
        os.system('net user ' + account + ' ' + password)
        gui.buttonbox(
            msg='Password changed successfully!',
            title='Change Password',
            choices=['Back']
        )
        main()

    else:
        gui.buttonbox(
            msg='Password change cancelled!',
            title='Change Password',
            choices=['Back']
        )
        main()

main()
