import os 

from flask import Flask, render_template

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

@app.route('/contact')
def contact():
    contact_form = ContactForm()
    contact_form.submit(class_ = 'hola')
    return render_template('contact.html', form = contact_form)

if __name__=='__main__':
    app.run(debug=True)