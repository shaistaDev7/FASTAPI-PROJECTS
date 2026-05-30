from pydantic import BaseModel,EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List,Dict,Optional, Annotated 
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name")]
    Email:EmailStr
    age:int=Field(gt=0, lt=120)
    weight:Annotated[float, Field(gt=0,strict=True)]
    married:bool
    allergies: Optional[List[str]]=None
    contact:Dict[str,str]
    ########Model Validator##########
    #Field validation applied on single field. If we want two or more field validation then we use model validator
    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age>60 and not 'emergency'in model.contact:
            raise ValueError('Person old than must be emergency contact')
        return model

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)


data={'name':'Shaista', 'Email':'shaista@gcwus.com', 'age':30,'weight':45.6,'married':True, 'contact':{'phone':'0374858678'}}
patient1=Patient(**data)
insert_patient_data(patient1)
