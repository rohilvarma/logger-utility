from logger_utility import LoggerConfig, Logger


def main() -> None:
    # testing the logger
    config = LoggerConfig()
    logger = Logger(config)

    logger.info("Test Message")
    logger.debug("Debug test")
    logger.error("Error test")
    logger.warning("Warnig ")
    logger.info(config)
    logger.warning("ASDFASDf", config)
    logger.error("ERR", a)

if __name__ == "__main__":
    main()