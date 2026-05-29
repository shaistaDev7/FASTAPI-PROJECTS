from fastapi import FastAPI, Path, HTTPException, Query
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
    
    