import os 
import csv

from flask import Flask, render_template, flash, url_for, redirect
from forms import ContactForm
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor

from send_email import send_email

def csv_to_dict(archivo_csv):
    lista_diccionarios = []
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            lista_diccionarios.append(dict(fila))
    return lista_diccionarios

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
    # Opens a csv with data about the projects
    file_csv = 'projects.csv'
    projects_dict = csv_to_dict(file_csv)
    return render_template('projects.html', projects = projects_dict)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data 
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        send_email(name, email, phone, message)
        flash('Succesfuly send')
        return redirect(url_for('contact'))
    return render_template('contact.html', form = form)

if __name__=='__main__':
    app.run(debug=True)