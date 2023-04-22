import config
import pickle
import json
import numpy as np
class CardiovascularRiskPrediction():
    def __init__(self,id,age,education,sex,is_smoking,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose):
        self.id = id
        self.age = age
        self.education = education
        self.sex = sex
        self.is_smoking = is_smoking
        self.cigsPerDay = cigsPerDay
        self.BPMeds = BPMeds
        self.prevalentStroke = prevalentStroke
        self.prevalentHyp = prevalentHyp
        self.diabetes = diabetes
        self.totChol = totChol
        self.sysBP = sysBP
        self.diaBP = diaBP
        self.BMI = BMI
        self.heartRate = heartRate
        self.glucose = glucose
    
    def load_model(self):
        with open(config.model_file_path,'rb') as f:
            self.model = pickle.load(f) # model file instance is created because we have to use it further

        with open(config.json_file_path,'r') as f:
            self.json_data = json.load(f)  # it contain label encoded data and columns names

    def get_predicted_charges(self):
        self.load_model() # above function call here because we are going to use methods here
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.id
        test_array[1] = self.age
        test_array[2] = self.education
        test_array[3] = self.json_data['sex'][self.sex]
        test_array[4] = self.json_data['is_smoking'][self.is_smoking]
        test_array[5] = self.cigsPerDay
        test_array[6] = self.BPMeds
        test_array[7] = self.prevalentStroke
        test_array[8] = self.prevalentHyp
        test_array[9] = self.diabetes
        test_array[10] = self.totChol
        test_array[11] = self.sysBP
        test_array[12] = self.diaBP
        test_array[13] = self.BMI
        test_array[14] = self.heartRate
        test_array[15] = self.glucose
        predicted_charges = self.model.predict([test_array])
        return predicted_charges

