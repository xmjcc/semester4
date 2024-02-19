from flask import Flask
app = Flask(__NAME__)

def index():
    return "this is home page"