import os

from logger_utility.severity import Severity
from logger_utility.writer import LogWriter


class FileWriter(LogWriter):
    def __init__(self, path: str):
        super().__init__()
        self.__path = path
        self.__separator = "/" if "/" in self.__path else "\\"
        self.__file_open_mode = "a"
        self.__log_file_name = self.__path.split(self.__separator)[-1]

        if not os.path.exists(self.__path):
            self.__create_output_file()

    @property
    def file_open_mode(self):
        return self.__file_open_mode

    @file_open_mode.setter
    def file_open_mode(self, mode: str):
        if mode not in ("r", "a", "w", "x"):
            raise ValueError(f"Invalid file open mode: {mode}")

        self.__file_open_mode = mode

    def __create_output_file(self) -> None:
        """
        Creates the output log file and its parent directories if they do not exist.

        Raises:
            FileExistsError: If the log file already exists.

        Returns:
            None
        """
        split_path = self.__path.split(self.__separator)
        os.makedirs(self.__separator.join(split_path[:len(split_path) - 1]))

        self.__file_open_mode = "x"
        try:
            with open(self.__path, self.__file_open_mode) as f:
                f.write("")

            self.__file_open_mode = "a"

        except FileExistsError:
            raise FileExistsError(f"Log file: {self.__log_file_name} already exists.")

    def write(self, severity: Severity, message: str, detailed_message: str = None) -> None:
        time = self.get_current_time()
        formatted_string = self.log_format.format(time, severity.name, message)
        try:
            if severity not in Severity:
                raise ValueError(
                    f"Invalid severity requested: {severity}."
                )

            if detailed_message:
                formatted_string += f" : {detailed_message}"

            with open(self.__path, self.file_open_mode) as f:
                f.write(formatted_string + "\n")

        except Exception as e:
            print(Severity.ERROR.value["color"] + str(e) + "\033[0m")


if __name__ == "__main__":
    fw = FileWriter()
