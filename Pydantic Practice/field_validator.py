from pydantic import BaseModel,EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict,Optional, Annotated 
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name")]
    Email:EmailStr
    age:int=Field(gt=0, lt=120)
    weight:Annotated[float, Field(gt=0,strict=True)]
    married:bool
    allergies: Optional[List[str]]=None
    contact:Dict[str,str]
    ########Field Validator##########
    #Field validation applied on single field. If we want two or more field validation then we use model validator
    @field_validator('Email')
    @classmethod
    def email_validator(cls,value):
        valid_email=['gcwus.com','umt.com']
        valid_domain=value.split('@')[-1]
        if valid_domain not in valid_email:
            raise ValueError('Not a Valid Email')
        return value
    #Transform on name field
    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        return value.upper()
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
