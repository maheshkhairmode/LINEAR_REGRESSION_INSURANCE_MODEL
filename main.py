from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import MedicalInsurance
import config

app = Flask(__name__)
@app.route("/")
def Hello():
    print("welcome")
    return render_template("index.html")

@app.route("/predict_charges",methods=["POST","GET"])
def medical_insurance():

    if request.method=="POST":
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        medi_charges=MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges=medi_charges.Get_Medical_insurance()

        return render_template("index.html",prediction=charges)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)


