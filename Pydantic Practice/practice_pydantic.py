from pydantic import BaseModel,EmailStr, AnyUrl, Field
from typing import List,Dict,Optional, Annotated 
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name")]
    #Used to validate email
    Email:EmailStr
    #Used to validate url
    #Linked_URL: AnyUrl
    age:int=Field(gt=0, lt=120)
    weight:float
    married:bool
    #Used for Optional
    allergies: Optional[List[str]]=None
    contact:Dict[str,str]
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)


data={'name':'Shaista', 'Email':'shaista@gmail.com', 'age':30,'weight':45.6,'married':True, 'contact':{'phone':'0374858678'}}
patient1=Patient(**data)
insert_patient_data(patient1)
