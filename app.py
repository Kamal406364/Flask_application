import flask
from flask import Flask,  request,jsonify
import json

app = Flask(__name__)


def validate_password(password):
    l=[char for char in password]
    if len(l)>=8:
        uppercase=any(i.isupper() for i in  l)
        if uppercase:
            lowercase=any(i.islower() for i in l)
            if lowercase:
                digit=any(i.isdigit() for i in l)
                if digit:
                    special_char=any(i in "!@#$%^&*"  for i in l)
                    if special_char:
                        return True
                    else:
                        return "should contain special characters"
                else:
                    return "should contain minimum one digit"
            else:
                return "should contain minimum one lowercase"
        else:
            return "should containi minimum one uppercase"
    else:
        return "should contain minimum 8 characters"

    return  False
    

# def uppercase(string):
#     return string.upper()

# def lowercase(string):
#     return string.lower()

# def captilize_string(string):
#     return  string.capitalize()

# def find_character(a,string):
#     return string.find(a)

# def join_string(a,b):
#     return ' '.join([a,b])



@app.route('/validate', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.data)
        d = json.loads(request.data)
        print(d)
        password = d['password']
        message = validate_password(password)
    
        return jsonify({"message":message})
    
@app.route('/uppercase',methods=['GET','POST'])
def upper():
    if request.method=='POST':
        d=json.loads(request.data)
        string1=d['word']
        result=string1.upper()
        return jsonify({"result":result})
    
@app.route('/lowercase',methods=['GET','POST'])
def lower():
    if request.method=='POST':
        d=json.loads(request.data)
        string1=d['word']
        result=string1.lower()
        return jsonify({"result":result})

@app.route('/capitalize',methods=['GET','POST'])
def capitalize():
    if request.method=='POST':
        d=json.loads(request.data)
        string1=d['word']
        result=string1.capitalize()
        return jsonify({"result":result})
    
@app.route('/find',methods=['GET','POST'])
def find_char_route():
    if request.method=='POST':
        d=json.loads(request.data)
        char_=d['char']
        string1=d['word']
        result=string1.find(char_)
        return jsonify({"result":result})
    
@app.route('/join', methods=['GET','POST'])
def join():
    if request.method=='POST':
        d=json.loads(request.data)
        string1=d['a']
        string2=d['b']
        result=' '.join([string1,string2])

        return jsonify({"result":result})
    
if __name__ == '__main__':
    app.run(debug=True)
