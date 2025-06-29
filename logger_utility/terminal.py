from datetime import datetime

from logger_utility.writer import LogWriter
from logger_utility.severity import Severity

class TerminalWriter(LogWriter):
    def __init__(self):
        super().__init__()
        self.__RESET_COLOR = "\033[0m"

    def write(self, severity: Severity, message: str, detailed_message: str = None) -> None:
        try:
            if severity not in Severity:
                raise ValueError(
                    f"Invalid severity requested: {severity}."
                )

            time = self.get_current_time()
            formatted_string = self.log_format.format(time, severity.name, message)

            if detailed_message:
                formatted_string += f" : {detailed_message}"

            print(severity.value["color"] + formatted_string + self.__RESET_COLOR)

        except ValueError as e:
            print(Severity.ERROR.value["color"] + str(e) + self.__RESET_COLOR)


if __name__ == "__main__":
    tw = TerminalWriter()
    tw.write("WARNING", "Test", "Detailed")
    tw.write("INFO", "Test")
    tw.write("INFO", "Test", "Detailed")
    tw.write("warning", "Test", "Detailed")
