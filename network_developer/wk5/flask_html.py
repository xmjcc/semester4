
from flask import Flask, render_template

app = Flask(__name__)

# Sample data list
data_list = [  {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 35}]

@app.route('/')
def index():
    # Pass the data list to the HTML template
    return render_template('index.html', users=data_list)

if __name__ == '__main__':
    app.run(debug=True)