
# import the Flask class from the flask module
from flask import Flask , render_template, send_from_directory
from flask_wtf import FlaskForm


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

@app.route('/Data')
def Data():
    return render_template('Data_collection.html')

@app.route('/image')
def image():
    return send_from_directory('static','Uni_Glasgow_1.jpeg')



# start the development server using the run() method
if __name__ == '__main__':
    
    # host = 0.0.0.0 will use the local ip adress and the local host to run the website
    # debug = True will allow the website to be 'update' while I change the code
    app.run ( host='0.0.0.0', debug=True , port=5555)