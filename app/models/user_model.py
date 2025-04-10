from pydantic import BaseModel, EmailStr, Field, field_validator

class BaseUser(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters long")

    @field_validator("password", mode="before")
    def validate_password(cls, value):
        if not value.strip():
            raise ValueError("Password cannot be empty or whitespace")
        return value

class User(BaseUser):
    username: str = Field(..., min_length=4, description="Username must be at least 4 characters long")

    @field_validator("username", mode="before")
    def validate_username(cls, value):
        if not value.strip():
            raise ValueError("Username cannot be empty or whitespace")
        return value

class UserLogin(BaseUser):
    pass