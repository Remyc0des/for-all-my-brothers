from flask import Flask, render_template, request
import requests
import json
from datetime import date

app = Flask(__name__)



@app.route("/")
def landing():
    
    return render_template('index.html')
  
@app.route("/list")
def response():
    
    response = requests.get(' https://api.846policebrutality.com/api/incidents?')
    data = response.json()

    
    print("DATA:",data)
    return render_template('list.html', data=data)

    

if __name__ == "__main__":
       app.run(debug=True, host='0.0.0.0', port='5001')


