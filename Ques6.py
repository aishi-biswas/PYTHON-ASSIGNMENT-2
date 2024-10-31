from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('usr')
        password=request.form.get('pwd')
        if username is None or password is None:
            return "Username or password not provided"
        x = re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*\-]).{8,}$", password)
        if '@' in username and x:
            return render_template('login.html')
        else:
            return "Login failed: Invalid username or password format"
    return render_template('index4.html')
    
if __name__=='__main__':
    app.run(debug=True)