from flask import Flask, render_template  
import zipfile        #The uppercase implies an object


app = Flask(__name__)            

students =['Palak', 'Allen', 'Charlie', 'Alley']



@app.route('/', methods = ['GET'])  #A decorator function that binds a path
                     #to an HTTP command (PUT, POST, DELETE) default is GET
def home():
    return 'This is the home page '
    # Create an instance of the StudentSurveyApp class from group.py

@app.route('/allstudents', methods=['GET'])  

def allstudents():
    
    return str(students)



# app.run(debug = True) 
if __name__=='__main__':          #app.run(host, port, debug, options)
    app.run(debug = True)              #app.run(host, port, debug, options)



