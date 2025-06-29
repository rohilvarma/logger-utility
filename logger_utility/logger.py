from logger_utility.config import LoggerConfig
from logger_utility.severity import Severity


class Logger:
    def __init__(self, config: LoggerConfig) -> None:
        self.__config = config

    def info(self, message: str, detailed_message: str = None) -> None:
        self.__log(Severity.INFO, message, detailed_message)

    def warning(self, message: str, detailed_message: str = None) -> None:
        self.__log(Severity.WARNING, message, detailed_message)

    def error(self, message: str, detailed_message: str = None) -> None:
        self.__log(Severity.ERROR, message, detailed_message)

    def debug(self, message: str, detailed_message: str = None) -> None:
        self.__log(Severity.DEBUG, message, detailed_message)

    def success(self, message: str, detailed_message: str = None) -> None:
        self.__log(Severity.SUCCESS, message, detailed_message)

    def __log(self, severity: Severity,  message: str, detailed_message: str = None) -> None:
        for w in self.__config.writers:
            w.write(severity, message, detailed_message)


if __name__ == "__main__":
    print(Severity.INFO)