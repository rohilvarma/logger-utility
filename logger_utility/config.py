from .file import FileWriter
from .terminal import TerminalWriter
from .writer import LogWriter


class LoggerConfig:
    def __init__(self, log_output_path: str = None, debug: bool = None, datetime_format: str = None):
        self.log_output_path = log_output_path
        self.debug = debug
        self.datetime_format = datetime_format
        self.writers = self.__create_writers()
        self.__update_writer_attributes()

    def __create_writers(self) -> list[LogWriter]:
        writers = [TerminalWriter()]
        if self.log_output_path:
            writers.append(FileWriter(self.log_output_path))

        return writers

    def __update_writer_attributes(self) -> None:
        for w in self.writers:
            w.debug_mode = self.debug if self.debug is not None else w.debug_mode
            w.datetime_format = self.datetime_format if self.datetime_format is not None else w.datetime_format

    def __str__(self) -> str:
        return f"LoggerConfig(log_output_path={self.log_output_path}, debug={self.debug}, writers={[type(w).__name__ for w in self.writers]})"


if __name__ == "__main__":
    config = LoggerConfig("~/Desktop/Dev-Folder/lld-hands-on-projects", True)
    print(config)
