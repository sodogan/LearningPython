import logging as log


def main():
    # You can only configure logging one time before actual logging starts
    # subsequent calls will have no effect
    # log.basicConfig(level=log.DEBUG)
    log.basicConfig(level=log.WARNING, filename="output.log", filemode="w")
    log.debug("debug-level message")
    log.info("info-level message")
    log.warning("warning-level message")
    log.error("error-level message")
    log.critical("critical-level message")


if __name__ == "__main__":
    main()
