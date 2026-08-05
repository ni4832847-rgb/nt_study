from pydantic import BaseModel, Field, field_validator

def validate_task_name(value):
    if value.strip() == "":
        raise ValueError("Task name must not be blank")
    return value

class TaskCreate(BaseModel):
    name: str = Field(min_length=1)
    status: str = "未完成"

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value):
        return validate_task_name(value)


class TaskUpdate(BaseModel):
    name: str = Field(min_length=1)
    status: str

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value):
        return validate_task_name(value)

class Task(BaseModel):
    id: int
    name: str
    status: str