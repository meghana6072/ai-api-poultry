import pickle
from flask import Flask,request

api=Flask(_name_)

with open('ai.pkl','rb') as f:
    ai=pickle.load(f)

@api.route('/')
def home():
    return"API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    T=request.args.get('T')
    T=float(T)
    P=request.args.get('P')
    P=float(P)
    data=[[T,P]]
    response=ai.predict(data)[0]
    return response

if _name=="main_":
    api.run(
        host='0.0.0.0',
        port=2000
    )  APP.PY