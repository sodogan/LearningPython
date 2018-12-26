import logging as log

extData = {
    'user': 'joem@example.com'
}


def main():
    # You can only configure logging one time before actual logging starts
    # subsequent calls will have no effect
    # log.basicConfig(level=log.DEBUG)
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M%S %p"
    log.basicConfig(level=log.DEBUG, format=fmtstr, datefmt=datestr)
    log.debug("debug-level message", extra=extData)
    log.info("info-level message", extra=extData)
    log.warning("warning-level message", extra=extData)
    log.error("error-level message", extra=extData)
    log.critical("critical-level message", extra=extData)


if __name__ == "__main__":
    main()
