import os

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

    def write(self, severity: str, message: str, detailed_message: str = None) -> None:
        pass

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

if __name__ == "__main__":
    fw = FileWriter()
