from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal


class Student(BaseModel):
    name: str = "tofa"
    age: Optional[int] = None
    email: EmailStr
    CGPA: float = Field(gt=0, lt=5, default=3, description="It represents CGPA")
    hobby: list[str] = Field(description="List of student hobby")
    attendence: Literal["good", "Bad"] = Field(
        description="is student attentive or note?"
    )


new_student = {
    "name": "tofaal",
    "age": 30,
    "email": "cse@gmail.com",
    "CGPA": 3,
    "hobby": {"swim", "read"},
    "attendence": "good",
}


student = Student(**new_student)

print(dict(student))
student_JSON = student.model_dump_json
print(student_JSON)
