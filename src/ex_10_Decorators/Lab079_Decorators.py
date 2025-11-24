"""
def add_security(func):


    def wrapper():
        print("1. Before the function called")
        print("2. Add helmet, dashcash, gloves, Knee guards, life jacket")
        func()
        print("3. After the function called")
        print("4. Secure Driving, Leave all the items")
    return wrapper


@add_security
def drive_ola_scooter():
    print("I'm driving ola scooter")

@add_security
def drive_zypto_scooter():
    print("I'm driving zypto scooter")
"""

def add_login_process(func):
    def wrapper():

        print("1. Before the function called")
        print("2. login the Device")
        print("3. login to the website")
        func()
        print("4. After the function called")
        print("5. Logot to the website/n")
        print("-------------------")
    return wrapper



@add_login_process
def online_cloth_shopping():
    print("I'm shopping on Zara online")
@add_login_process
def online_jewel_shopping():
    print("I'm shopping on Swarovski online")
