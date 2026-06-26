from enum import Enum

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    SHORTLISTED = "SHORTLISTED"
    REJECTED = "REJECTED"
    SELECTED = "SELECTED"