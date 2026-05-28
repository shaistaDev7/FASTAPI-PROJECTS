from fastapi import FastAPI
import json
def load_data():
    with open("patients.json", 'r') as f:
        data=json.load(f)
        return data
app=FastAPI()
@app.get("/")
def hello(): 
    return {'message':'Hello World'}

@app.get("/about")
def about(): 
    return {'message':'This is website provide AI related services'}
@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/Patient/{patient_id}")
def View_patient(patient_id: str):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    return {"Error": "Data NOT Found"}
