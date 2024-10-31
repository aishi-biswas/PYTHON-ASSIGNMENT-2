from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getTemp():
    result = None
    if request.method=='POST':
        celsius=float(request.form.get('temp'))
        fahrenheit=celsius*(9/5)+32
        result = fahrenheit
    return render_template('index6.html', result=result)

if __name__=='__main__':
    app.run(debug=True)