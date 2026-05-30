from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field, computed_field
from typing import Annotated, Literal
import json
class patient(BaseModel):
    id:Annotated[str,Field(...,description='Patient Id',example='P001')]
    name:Annotated[str,Field(..., description="Patient Name")]
    city:Annotated[str,Field(..., description="Patient City Name")]
    age:Annotated[int,Field(..., gt=0, description="Patient Age")]
    gender:Annotated[Literal['Male','Female','Other'], Field(..., description="Geneder")]
    height:Annotated[float,Field(...,gt=0, description="Patient Height")]
    weight:Annotated[float,Field(...,gt=0, description="Patient Weight")]
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        else:
            return 'Obese'

def load_data():
    with open("patients.json", 'r') as f:
        data=json.load(f)
        return data
def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data,f)
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
def View_patient(patient_id: str=Path(..., example="P001")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail="Data NOT Found")


@app.get("/Sorted")
def Sorted(
    sorted_by: str = Query(..., description="Sort by height, weight, or bmi"),
    Order_by: str = Query("asc", description="Order: asc or desc")
):
    
    valid_fields = ["height", "weight", "bmi"]
    
    # Check valid field
    if sorted_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Select from {valid_fields}")
    
    # Check order
    if Order_by not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Select from ['asc', 'desc']")
    
    data = load_data()
    
    # Sorting
    reverse = True if Order_by == "desc" else False
    
    sorted_data = sorted(data, key=lambda x: x[sorted_by], reverse=reverse)
    
    return sorted_data
    
@app.post('/created')
def patient_created(patient:patient):
    #Load Existing Data
    data=load_data()
    #Check if patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail="patient already exist")
    #Add new patient into database
    data[patient.id]=patient.model_dump(exclude=['id'])
    
    #Save data into jason file
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'Data Successfulyy Submitted'})