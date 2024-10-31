from flask import Flask, render_template, redirect, request, url_for
import random

app = Flask(__name__)

quotes=['"The only way to do great work is to love what you do." — Steve Jobs', '"Success is not final, failure is not fatal: It is the courage to continue that counts." — Winston Churchill', '"Believe you can and you are halfway there." — Theodore Roosevelt', '"The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt', '"It always seems impossible until it is done." — Nelson Mandela']
@app.route('/quote')
def quote():
    result=(random.choice(quotes))
    return render_template('index3.html', result=result)

if __name__=='__main__':
    app.run(debug=True)