from pydantic import BaseModel,EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict,Optional, Annotated 
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name")]
    #Used to validate email
    Email:EmailStr
    #Used to validate url
    #Linked_URL: AnyUrl
    age:int=Field(gt=0, lt=120)
    #gt=0 means greater than 0 constrant and strict=True not allow string value
    weight:Annotated[float, Field(gt=0,strict=True)]
    married:bool
    #Used for Optional
    allergies: Optional[List[str]]=None
    contact:Dict[str,str]
    ########Field Validator##########
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
