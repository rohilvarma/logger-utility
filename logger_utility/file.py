import os

from .writer import LogWriter


class FileWriter(LogWriter):
    def __init__(self, path: str):
        self.__path = path
        self.__separator = "/" if "/" in self.__path else "\\"
        self.__file_open_mode = "a"
        self.__log_file_name = self.__path.split(self.__separator)[-1]

        if not os.path.exists(self.__path):
            self.__create_output_file()

    def write(self, severity: str, message: str):
        pass

    def __create_output_file(self):
        split_path = self.__path.split(self.__separator)
        os.makedirs(self.__separator.join(split_path[:len(split_path) - 1]))

        try:
            with open(self.__path, "x") as f:
                f.write("")

        except FileExistsError:
            raise FileExistsError(f"Log file: {self.__log_file_name} already exists.")


    def update_file_open_mode(self, mode: str) -> None:
        if mode not in ("r", "a", "w", "x"):
            raise ValueError(f"Invalid file open mode: {mode}")

        self.__file_open_mode = mode


if __name__ == "__main__":
    fw = FileWriter()
