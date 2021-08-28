#BMI_Calculator

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

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
        get1 = (18.5*height_sq)/703 - weight_p #get1 and get2 are the variables that calculate the weight to gain or to lose.
        get2 = (25*height_sq)/703 - weight_p

        if ((BMI >= 18.5) and (BMI <= 25)):
            print("Great. Maintain your current healphy weight.")

        elif ((BMI > 16) and (BMI <18.5)):
            print("You are underweight.")
            print("To get to the healthy weight you need to gain from",int(get1),"to",int(get2),"pounds.")

        elif (BMI <= 16):
            print("You are severely underweight.")
            print("To get to the healthy weight you need to gain from",int(get1),"to",int(get2),"pounds.")

        elif ((BMI > 25) and (BMI < 30)):
            print("You are overweight.") 
            print("To get to the healthy weight you need to lose from",int(-get2),"to",int(-get1),"pounds.")

        else:
            print("You are severely overweight.")
            print("To get to the healthy weight you need to lose from",int(-get2),"to",int(-get1),"pounds.")

    return render_template("index.html", BMI = BMI)

if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code 
    # everytime there is an update in the code.
    app.run(debug=True)
