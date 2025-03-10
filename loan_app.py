from flask import Flask , request
import pickle

app = Flask(__name__)

with open("classifier.pkl","rb") as f :
   model = pickle.load(f)

@app.route("/")
def home_page():
    return ("<h1> LOAN APPROVAL APPLICATION</h1>")

@app.route("/predict",methods = ['GET',"POST"])
def predict():
    if request.method == "GET":
        return ("Sure, I will make the prediction")
    else :
        loan_r = request.get_json()
        if loan_r['Gender'] == "Male":
            Gender = 0
        else : 
            Gender = 1
        
        if loan_r['Married'] == "No":
            Married = 0
        else : 
            Married = 1

        ApplicantIncome = loan_r['ApplicantIncome']
        LoanAmount = loan_r['LoanAmount']
        Credit_History = loan_r['Credit_History']

        pred = model.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])

        if pred == 0 :
            result = "Rejected"
        else : 
            result = "Accepted"
         
        return {"Loan Approval Status": result}
