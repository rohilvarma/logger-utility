from datetime import datetime

from .writer import LogWriter


class TerminalWriter(LogWriter):
    def __init__(self):
        super().__init__()
        self.__colors = {
            "INFO": '\033[94m',
            "WARNING": '\033[93m',
            "ERROR": '\033[91m',
            "RESET": '\033[0m',
            "SUCCESS": '\033[92m',
            "DEBUG": "\033[37m",
        }

    def write(self, severity: str, message: str, detailed_message: str = None) -> None:
        try:
            if severity not in self.__colors:
                raise ValueError(
                    f"Invalid severity requested: {severity}. Allowed severities are {list(self.__colors.keys())}"
                )

            time = datetime.now().strftime(self.datetime_format)
            formatted_string = self.log_format.format(time, severity, message)

            if detailed_message:
                formatted_string += f" : {detailed_message}"

            print(self.__colors[severity] + formatted_string + self.__colors["RESET"])

        except ValueError as e:
            print(self.__colors["ERROR"] + str(e) + self.__colors["RESET"])


if __name__ == "__main__":
    tw = TerminalWriter()
    tw.write("WARNING", "Test", "Detailed")
    tw.write("INFO", "Test")
    tw.write("INFO", "Test", "Detailed")
    tw.write("warning", "Test", "Detailed")
