from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/projects')
def about_me():
    return render_template('projects.html')

@app.route('/contact')
def about_me():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)