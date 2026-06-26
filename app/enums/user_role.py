from enum import ENUM

class UserRole(str, ENUM):
    STUDENT = "STUDENT"
    HR = "HR"
    TPO = "TPO"