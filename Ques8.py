from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

fb_dict={}
@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method=='POST':
        name=request.form.get("name")
        feedback=request.form.get("fb")
        if name and feedback:
            fb_dict[name]=feedback
        return redirect(url_for("feedback"))
    return render_template('index7.html',fb_dict=fb_dict)

if __name__=='__main__':
    app.run(debug=True)