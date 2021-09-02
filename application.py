from flask import Flask
from flask import render_template
from flask import request

application = app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def Calculate():
    BMI = ''
    if request.method == 'POST' and 'weight_p' in request.form and 'height_f' in request.form and 'height_in' in request.form:
    
        #Declare all variables.
        weight_p = int(request.form.get("weight_p"))   
        height_f = int(request.form.get("height_f")) 
        height_in = int(request.form.get("height_in")) 
        #Formular that convert the height in Inches
        height_sq = ((height_f*12) + height_in)**2 

        BMI = round((weight_p/height_sq)*703, 2) #Formular that calculate the BMI.

    return render_template("index.html", BMI = BMI)
