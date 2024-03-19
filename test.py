
# import the Flask class from the flask module
from flask import Flask , render_template, send_from_directory, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange
import secrets

# create the application object
app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = secrets.token_hex(16)

print(app.config['SECRET_KEY'])

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
    email = StringField('Email', validators= [DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])

class SatisfactionForm(FlaskForm):
    satisfaction = IntegerField('Grade Satisfaction (1-10)', validators=[NumberRange(min=1, max=10)])
    suggestion = TextAreaField('please put your suggestion here')

class GradesForm(FlaskForm):
    math = SelectField('Math', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    english = SelectField('English', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    programming = SelectField('Programming', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])

data_file = 'student_data.txt'

def write(data):
    with open(data_file, 'a') as file:
        file.write(data + '\n')

@app.route('/Data', methods=['GET', 'POST'])
def Data():
    student_detail = StudentDetail()
    satisfaction_form = SatisfactionForm()
    grades_form = GradesForm()
    
    if request.method == 'POST':
        if student_detail.validate_on_submit() and satisfaction_form.validate_on_submit() and grades_form.validate_on_submit():
            name = student_detail.name.data
            email = student_detail.email.data
            student_number = student_detail.student_number.data
            satisfaction = satisfaction_form.satisfaction.data
            suggestion = satisfaction_form.suggestion.data
            math_grade = grades_form.math.data
            english_grade = grades_form.english.data
            programming_grade = grades_form.programming.data

            data = f'Name: {name}, Email: {email}, Student Number: {student_number}, Satisfaction: {satisfaction}, Suggestion: {suggestion}, Math Grade: {math_grade}, English Grade: {english_grade}, Programming Grade: {programming_grade}'

            write(data)

            return 'Data has been submitted'
        else:
            # Render the template with the forms and their respective error messages
            return render_template('Data_collection.html', student_detail=student_detail, satisfaction_form=satisfaction_form, grades_form=grades_form)

    # Render the template with the forms if the request method is GET
    return render_template('Data_collection.html', student_detail=student_detail, satisfaction_form=satisfaction_form, grades_form=grades_form)

    




@app.route('/image')
def image():
    return send_from_directory('static','Uni_Glasgow_1.jpeg')



# start the development server using the run() method
if __name__ == '__main__':
    
    # host = 0.0.0.0 will use the local ip adress and the local host to run the website
    # debug = True will allow the website to be 'update' while I change the code
    app.run ( host='0.0.0.0', debug=True , port=5555)