from flask import Flask, request          #The uppercase implies an object


app = Flask(__name__)            



# def generate_page():                       #to an HTTP command (PUT, POST, DELETE) default is GET
#     return 'hello world'
def index():                       #to an HTTP command (PUT, POST, DELETE) default is GET
    return '1111hello wdfddffforld yo arfdfdfe the dddddbet1111'

# @app.route('/home', methods = ['GET'])  #A decorator function that binds a path
#                      #to an HTTP command (PUT, POST, DELETE) default is GET
# def home():
#     return index()
    # Create an instance of the StudentSurveyApp class from group.py
    
# @app.route('/<name>', methods = ['GET'])  #A decorator function that binds a path
#                      #to an HTTP command (PUT, POST, DELETE) default is GET
# def centennial(name):
#     return f'welcome {name} to centennial college'
#     # Create an instance of the StudentSurveyApp class from group.py
# def indexwww():
#     return generate_page()

@app.route('/home', methods = ['GET'])  #A decorator function that binds a path
                     #to an HTTP command (PUT, POST, DELETE) default is GET
def home():
    return index()
    # Create an instance of the StudentSurveyApp class from group.py

@app.route('/verbs', methods='GET POST TRACE'.split())             
def show_verbs():
    return f'You have used the {request.method} command'



app.run(debug = True) 
# if __name__=='__main__'            #app.run(host, port, debug, options)
#     app.run(debug = True)              #app.run(host, port, debug, options)



