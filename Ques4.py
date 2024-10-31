from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

tasks=[]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        task=request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index'))
    return render_template('index2.html', tasks=tasks)

if __name__=='__main__':
    app.run(debug=True)