import pandas as pandas
import numpy as np 
import pickle
import json
import config

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def Load_models(self):

        with open("models\insurance_model.pkl","rb")as f:
            self.model=pickle.load(f)

        with open("models\data.json","r")as f:
            self.data=json.load(f)
    
    def Get_Medical_insurance(self):

        self.Load_models()
        region_index=self.data["columns"].index(self.region)


        array=np.zeros(len(self.data["columns"]))
        array[0]=self.age
        array[1]=self.data["sex"][self.sex]
        array[2]=self.bmi
        array[3]=self.children
        array[4]=self.data["smoker"][self.smoker]
        array[region_index]=1

        print("array is",array)
        predicted_charges=self.model.predict([array])[0]
        print(predicted_charges)
        return np.around(predicted_charges,2)

if __name__ =="__main__":

    age=40
    sex="male"
    bmi=25
    children=1
    smoker="yes"
    region="southwest"

    medi_charges=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=medi_charges.Get_Medical_insurance()
    print("predicted insurance charges is ",charges)
    





    





