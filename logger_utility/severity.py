from enum import Enum

class Severity(Enum):
    SUCCESS = {
        "level": 1,
        "color": "\033[92m"
    }
    DEBUG = {
        "level": 2,
        "color": "\033[37m"
    }
    INFO = {
        "level": 3,
        "color": "\033[94m"
    }
    WARNING = {
        "level": 4,
        "color": "\033[93m"
    }
    ERROR = {
        "level": 5,
        "color": "\033[91m"
    }


if __name__ == "__main__":
    print(Severity.INFO.value["level"])