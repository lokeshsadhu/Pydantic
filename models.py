from pydantic import BaseModel,confloat,validator,Field,ConfigDict,model_validator
from datetime import date,datetime,timedelta
from enums import DepartmentEnum
from typing import Literal
import uuid

    
class Module(BaseModel):
    id:int|uuid.UUID
    name:str
    professor:str
    credits:Literal[10,20]
    registration_code:str

class Student(BaseModel):
    id:uuid.UUID
    name:str
    date_of_birth:date=Field(default_factory=lambda: datetime.today().date())
    GPA:confloat(ge=0,le=5)
    course:str|None
    department:DepartmentEnum
    fees_paid:bool
    modules:list[Module]=Field(default=[],max_items=10)
    
    # model_config = ConfigDict(extra='allow',title='Student Model')
    
    @model_validator
    def validate_gpa_and_dept(values):
        dept=values.get('department')
        gpa=values.get('GPA')
        dept_science=dept==DepartmentEnum.SCIENCE_AND_ENGINEERING.value
        valid_gpa=gpa>=3.0
        if dept_science:
            if not valid_gpa:
                raise ValueError ('GPA not high enough for S&E')
        return values
    
    @validator('modules')
    def validate_module_length(cls,value):
        if(len(value) and len(value)!=3):
            raise ValueError("The modules length should be 3")
        return value
    
    @validator('GPA')
    def validate_gpa(cls,value,values):
        print(value)
    
    @validator('date_of_birth')
    def ensure_16_years_above(cls,value):
        sixteen_years_ago=datetime.now()-timedelta(days=365*16)
        sixteen_years_ago=sixteen_years_ago.date()
        
        if value>sixteen_years_ago:
            raise ValueError("Too young to enroll, sorry")
        return value
