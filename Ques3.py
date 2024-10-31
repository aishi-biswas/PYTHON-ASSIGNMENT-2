from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def enterNums():
    return render_template('index1.html')

@app.route('/add', methods=['POST'])
def addNums():
    number1=float(request.form['number1'])
    number2=float(request.form['number2'])
    result=number1+number2
    return render_template('index1.html', result=result)

if __name__=='__main__':
    app.run(debug=True)
