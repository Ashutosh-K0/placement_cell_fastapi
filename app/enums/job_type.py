from enum import Enum

class JobType(str, Enum):
    FULL_TIME = "FULL_TIME"
    INTERNSHIP = "INTERNSHIP"
    CONTRACT = "CONTRACT"