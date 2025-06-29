from abc import ABC, abstractmethod


class LogWriter(ABC):
    """
    Abstract base class for log writers.

    Provides properties for debug mode, datetime format, and log format.
    Subclasses must implement the write method to handle log output.

    Attributes:
        __debug_mode (bool): Enabl
        __datetime_format (str): Format string for timestamps.
        __log_format (str): Format string for log messages.
    """
    def __init__(self):
        self.__debug_mode = False
        self.__datetime_format = "%Y-%m-%d %H:%M:%S"
        self.__log_format = "{} | {} | {}"

    @property
    def debug_mode(self):
        return self.__debug_mode

    @debug_mode.setter
    def debug_mode(self, mode: bool):
        self.__debug_mode = mode

    @property
    def datetime_format(self):
        return self.__datetime_format

    @datetime_format.setter
    def datetime_format(self, dt_format: str):
        self.__datetime_format = dt_format

    @property
    def log_format(self):
        return self.__log_format

    @abstractmethod
    def write(self, severity: str, message: str, detailed_message: str = None) -> None:
        pass


if __name__ == "__main__":
    lw = LogWriter()