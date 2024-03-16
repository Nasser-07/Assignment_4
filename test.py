
# import the Flask class from the flask module
from flask import Flask 

# create the application object
app = Flask(__name__)

# use the decorator pattern to specify the URL(pathway) for the function
@app.route('/')

# def index is a function that will return the things that will be seen on the website 
# for now it is just hellow world
def index():
    return '<h1>Hello, World!</h1>' 


# start the development server using the run() method
if __name__ == '__main__':
    
    # host = 0.0.0.0 will use the local ip adress and the local host to run the website
    # debug = True will allow the website to be 'update' while I change the code
    app.run ( host='0.0.0.0', debug=True , port=5555)