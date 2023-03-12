from flask import Flask, render_template, request
import numpy as np
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("prediction_service/model.pkl","rb")
model = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def index():
    if request.method == "POST":

        url = request.form["input"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =model.predict(x)[0]

        #1 is safe       
        #-1 is unsafe
        
        y_pro_phishing = model.predict_proba(x)[0,0]
        y_pro_non_phishing = model.predict_proba(x)[0,1]
       
        if y_pred == 1:
            result = f"The site {y_pred} {url} is {round(y_pro_non_phishing,2)*100}% safe"
        else:
            result = f"The site {y_pred} {url} is {round(y_pro_phishing,2)*100}% unsafe"
        return render_template('index.html',result = result)
    return render_template("index.html")

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
