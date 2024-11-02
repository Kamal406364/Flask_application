user_db={
    'Thiru':{
        'password':'Thiru9494'
    },
    'Raj':{
        'password':'Raja1234'
    }   
}

def login(username,pass_word):
    global user_db
    # print(user_db[username]['password'])
    print(user_db.keys())
    keys_list = list(user_db.keys())
    print(username in keys_list)
    if username in user_db.keys():
        print(user_db[username]['password'])
        if user_db[username]['password']==pass_word:
            return True
        else:
            print("Invalid password")
            return False
    else:
        print ("username is not found")
        return False


def signin(func):
    def wrapper(*args,**kwargs):
        print("Args",*args)
        print("Kargs",type(args))

        username = args[0]
        password = args[1]
        
        

        if login(username, password):
            print("login successful")
            return func(username, password)
            
        else:
            print("login failed")
    return  wrapper

@signin
def login_page(username, password):
    pass

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_page(username, password)

main()
        

