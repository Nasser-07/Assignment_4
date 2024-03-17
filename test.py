
# import the Flask class from the flask module
from flask import Flask , render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange



# create the application object
app = Flask(__name__,template_folder='templates')

# use the decorator pattern to specify the URL(pathway) for the function
@app.route('/')
@app.route('/Welcome')
# def index is a function that will return the things that will be seen on the website 
# for now it is just hellow world
def index():
    return render_template('Welcome_page.html')


@app.route('/Info')
def Info():
    return render_template('Info.html')

class StudentDetail(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    student_number = StringField('Student Number', validators=[DataRequired()])

class SatisfactionForm(FlaskForm):
    satisfaction = IntegerField('Grade Satisfaction (1-10)', validators=[NumberRange(min=1, max=10)])
    suggestion = TextAreaField('please put your suggestion here')

class GradesForm(FlaskForm):
    math = SelectField('Math', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    science = SelectField('Science', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    history = SelectField('History', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])


@app.route('/Data', methods=['GET', 'POST'])
def Data():
    Student_Detail = StudentDetail()
    Satisfaction_Form = SatisfactionForm()
    Grades_Form = GradesForm()
    if student_detail.validate_on_submit() and satisfaction_form.validate_on_submit() and gra
    return render_template('Data_collection.html',StudentDetail=StudentDetail, SatisfactionForm=SatisfactionForm, GradesForm=GradesForm)


@app.route('/image')
def image():
    return send_from_directory('static','Uni_Glasgow_1.jpeg')



# start the development server using the run() method
if __name__ == '__main__':
    
    # host = 0.0.0.0 will use the local ip adress and the local host to run the website
    # debug = True will allow the website to be 'update' while I change the code
    app.run ( host='0.0.0.0', debug=True , port=5555)