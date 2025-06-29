from logger_utility import LoggerConfig, Logger


def main() -> None:
    # testing the logger
    config = LoggerConfig(
        debug=False,
        log_output_path="/Users/rohilvarma/Desktop/Dev-Folder/lld-hands-on-projects/logger-utility/logs/test.log"
    )
    logger = Logger(config)

    logger.info("Test Message")
    logger.debug("Debug test")
    logger.error("Error test")
    logger.warning("Warnig ")
    logger.info(config)
    logger.warning("ASDFASDf", config)
    logger.error("ERR", "ASDF")
    logger.success("Success!", "Testing success")

if __name__ == "__main__":
    main()