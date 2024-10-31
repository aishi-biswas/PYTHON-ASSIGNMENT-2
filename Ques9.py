from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

user_data={}

@app.route('/', methods=['GET', 'POST'])
def user_details():
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        city=request.form.get('city')
        if name and age and city:
            user_data[name]=[age,city]
        return redirect(url_for('user_details'))
    return render_template('index8.html', user_data=user_data)

if __name__=='__main__':
    app.run(debug=True)