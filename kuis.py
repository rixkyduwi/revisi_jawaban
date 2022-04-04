#cara menghitung BMI pria

import os

from flask import Flask,jsonify,request



app = Flask(__name__)

@app.route("/kuisilham", methods=["POST"])

def kuis():

    height =(float) (request.form['height'])

    weight =(float) (request.form['weight'])



    ideal = (float)(weight / (height/100)*(10/100))

    if ideal <= 18.4:

        return(f"berat badan ideal anda : {ideal} "+"Kamu Kurus.")

    elif ideal <= 24.9:

        return(f"berat badan ideal anda : {ideal} "+"Kamu Sehat")

    elif ideal <= 39.9:

        return(f"berat badan ideal anda : {ideal} "+"kamu gemuk.")

    else:

        return(f"berat badan ideal anda : {ideal} "+"kamu sangat gemuk, BAHAYA")

    

        

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug = True, port=4000)

