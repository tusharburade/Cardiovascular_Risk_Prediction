from flask  import Flask,jsonify,request,render_template
import config
app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('Welcome to flask')
    return 'Hello flask'

@app.route('/test')
def hello():
    return 'kkkkkk'

from project_app.utils import CardiovascularRiskPrediction
@app.route('/predicted_charges')
def get_Cardiovascular_Risk_Prediction():
    data = request.form
    id = eval(data['id']) #from postman we get string so converted in int	
    age = eval(data['age'])	
    education = eval(data['education'])
    sex = data['sex']	
    is_smoking = data['is_smoking']	
    cigsPerDay = eval(data['cigsPerDay'])
    BPMeds = eval(data['BPMeds'])
    prevalentStroke	= eval(data['prevalentStroke'])
    prevalentHyp	= eval(data['prevalentHyp'])
    diabetes	= eval(data['diabetes'])
    totChol	= eval(data['totChol'])
    sysBP	= eval(data['sysBP'])
    diaBP	= eval(data['diaBP'])
    BMI	= eval(data['BMI'])
    heartRate	= eval(data['heartRate'])
    glucose	= eval(data['glucose'])

    result_prediction = CardiovascularRiskPrediction(id,age,education,sex,is_smoking,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose)
    risk = result_prediction.get_predicted_charges()
    return jsonify ({'Result':f"Cardiovascular Risk Prediction is : {risk}"})
app.run()
