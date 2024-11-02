user_db={
    'Thiru':{
        'password':'Thiru9494'
    },
    'Raj':{
        'password':'Raja1234'
    }   
}

def login(username,pass_word):
    if username in user_db:
        if user_db[username]['password']==pass_word:
            return True
        else:
            print("Invalid password")
            return False
    else:
        print ("username is not found")
        return False


def signin(func):
    def wrapper():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            print("login successful")
            return func
        else:
            print("login failed")
    return  wrapper

@signin
def login_page():
    pass
login_page()
        

