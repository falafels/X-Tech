from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    idNum = TextField('ID Number:', validators=[validators.required()])
    name = TextField('Name:', validators=[validators.required()])
    gender = TextField('Gender:', validators=[validators.required()])
    DOB = TextField('Date of birth:', validators=[validators.required()])
    rmNum = TextField('Room number:', validators=[validators.required()])
    refphys = TextField('Referring Physician:', validators=[validators.required()])
    protocol = TextField('Protocol:', validators=[validators.required()])
    priority = TextField('Priority:', validators=[validators.required()])


 
 
@app.route("/", methods=['GET', 'POST'])
def form_info():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        idNum=request.form['idNum']
        name=request.form['name']
        gender=request.form['gender']
        DOB=request.form['DOB']
        rmNum=request.form['rmNum']
        refphys=request.form['refphys']
        protocol=request.form['protocol']
        priority=request.form['priority']
        print idNum, " ", name, " ", gender, " ", DOB, " ", rmNum, " ", refphys, " ". protocol, " ", priority
 
        if form.validate():
            # Save the comment here.
            flash('Form submitted for patient' + idNum)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('form_info.html', form=form)
 
if __name__ == "__main__":
    app.run()