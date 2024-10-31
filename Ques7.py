from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('index5.html')

if __name__=='__main__':
    app.run(debug=True)