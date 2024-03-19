
# import the Flask class from the flask module
from flask import Flask , render_template, send_from_directory, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange
import secrets

# create the application object
app = Flask(__name__,template_folder='templates')

# set up the secret key for the application the secref key is used to keep the client-side sessions secure 
app.config['SECRET_KEY'] = secrets.token_hex(16)

# print the secret key to the console just in case I need to use it 
print(app.config['SECRET_KEY'])

# I use the decorator pattern to specify the URL(pathway) for the function
# I used the standard decorator and /welcome just incase someone goes into the default webpage it will redirect them to the welcome page
@app.route('/')
@app.route('/Welcome')
# def index is a function that will return the things that will be seen on the website 
# I used it now to render my html welcome page 
# render template is a function that will render the html file that is in the templates folder
def index():
    return render_template('Welcome_page.html')

#I use the decorator pattern to specify the URL(pathway) for the function
# I define a function called infor that returns the render_template function that will render the html file that is in the templates folder
@app.route('/Info')
def Info():
    return render_template('Info.html')

# here I am creating a class called StudentDetail that will inherit from the FlaskForm class
# I am using the FlaskForm class to create a form that will allow me to collect data from the user
# this is replacing my html form 
class StudentDetail(FlaskForm):
    # I am creating a string field that will allow me to collect the name of the student
    # string field is similar to input type text in html were the user can input text but not a large amount just one line

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])

# I am creating a class called SatisfactionForm that will inherit from the FlaskForm class
# I am using the FlaskForm class to create a form that will allow me to collect data from the user
# IntegerField is similar to input type number in html were the user can input a number
# min and max just set the minimum number the user can input and the maximum
# TextAreaField is similar to input type text in html were the user can input a large amount of text
    
class SatisfactionForm(FlaskForm):
    satisfaction = IntegerField('Grade Satisfaction (1-10)', validators=[NumberRange(min=1, max=10)])
    suggestion = TextAreaField('please put your suggestion here')


# I am creating a class called GradesForm that will inherit from the FlaskForm class
# I am using the FlaskForm class to create a form that will allow me to collect data from the user
    # SelectField is similar to input type select in html were the user can select an option from a drop down menu like a multiple choice question 
    # choices is a list that will contain the options that the user can select from 
class GradesForm(FlaskForm):
    math = SelectField('Math', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    english = SelectField('English', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    programming = SelectField('Programming', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])


# I am creating a variable called data_file that will contain the name of the file that I will write the data to
data_file = 'student_data.txt'


# I am creating a function called write that will take in a parameter called data
# data is the data inputed by the user and extracted from the html file using jinja2 
# I am using the with statement to open the file and write the data to the file
def write(data):
    with open(data_file, 'a') as file:
        file.write(data + '\n')


#I use the decorator pattern to specify the URL(pathway) for the function with the methods GET and POST 
# I define a function called Data that will return the render_template function that will render the html file that is in the templates folder
# I am using the GET and POST methods to allow the user to input data and submit it
        # I am using the StudentDetail class to create a form that will allow me to collect data from the user
        # I am using the SatisfactionForm class to create a form that will allow me to collect data from the user
        # I am using the GradesForm class to create a form that will allow me to collect data from the user
        # I am using the validate_on_submit method to check if the form has been submitted and if the data is valid 
        # then define name and other pieces of data that will be extracted from the form and written to the file as a string by reffering to the classes which are basically the forms
        # I am using the write function to write the data to the file I also used formating to make the data look nice
        # I am returning a string that will tell the user that the data has been submitted
        # else I am returning the render_template function that will render the html file that is in the templates folder
        # If the method is not POST then I am returning the render_template function that will render the html file that is in the templates folder
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

            return render_template('Data_collection.html', student_detail=student_detail, satisfaction_form=satisfaction_form, grades_form=grades_form)

    return render_template('Data_collection.html', student_detail=student_detail, satisfaction_form=satisfaction_form, grades_form=grades_form)

    



# I use the decorator pattern to specify the URL(pathway) for the function
# this is the decaratot that I use to access the image that is in the static folder
# I use the send_from_directory function to send the image to the user and return the image
@app.route('/image')
def image():
    return send_from_directory('static','Uni_Glasgow_1.jpeg')



# start the development server using the run() method
if __name__ == '__main__':
    
    # host = 0.0.0.0 will use the local ip adress and the local host to run the website
    # debug = True will allow the website to be 'update' while I change the code
    app.run ( host='0.0.0.0', debug=True , port=5555)