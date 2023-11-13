import os 

from flask import Flask, render_template, flash, url_for, redirect
from forms import ContactForm
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor


app = Flask(__name__)
#Set up the Ckeditor field 
ckeditor = CKEditor(app)
#Adding bootstrap
Bootstrap5(app)
#Key required to CSRF
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')  

@app.route("/")
def about():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.email.data)
        print(form.phone.data)
        print(form.message.data)
        flash('Succesfuly send')
        return redirect(url_for('contact'))
    return render_template('contact.html', form = form)

if __name__=='__main__':
    app.run(debug=True)