from config import LoggerConfig


class Logger:
    def __init__(self, config: LoggerConfig) -> None:
        self.__config = config

    def info(self):
        pass

    def warning(self):
        pass

    def error(self):
        pass

    def debug(self):
        pass

    def __log(self):
        pass


if __name__ == "__main__":
    pass