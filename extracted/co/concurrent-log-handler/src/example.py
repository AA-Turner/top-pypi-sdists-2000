import logging
import logging.config
import time

"""
This is an example which shows how you can use ConcurrentLogHandler for synchronous logging.
ConcurrentLogHandler allows multiple processes to safely write to the same log file.

Note: The deprecated async logging functionality has been removed. For async logging,
consider using standard Python asyncio patterns with the synchronous handlers.
More information may be available in the README.md.
"""


def my_program():
    # Somewhere in your program, usually at startup or config time, you can
    # call your logging setup function. If you're in an multiprocess environment,
    # each separate process that wants to write to the same file should call the same
    # or very similar logging setup code.
    my_logging_setup()

    # Now for the meat of your program...
    logger = logging.getLogger("MyExample")
    logger.setLevel(logging.DEBUG)  # optional to set this level here

    for idx in range(20):
        time.sleep(0.05)
        print("Loop %d; logging a message." % idx)
        logger.debug("%d > A debug message.", idx)
        if idx % 2 == 0:
            logger.info("%d > An info message.", idx)
    print("Done with example; exiting.")


def my_logging_setup(log_name="example.log"):
    """
    An example of setting up logging in Python using a JSON dictionary to configure it.
    You can also use an outside .conf text file; see ConcurrentLogHandler/README.md
    """

    # Import this to install logging.handlers.ConcurrentRotatingFileHandler
    import concurrent_log_handler  # noqa: F401

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"},
            "example2": {
                "format": "[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s]"
                "[%(process)d][%(message)s]",
            },
        },
        # Set up our concurrent logger handler. Need one of these per unique file.
        "handlers": {
            "my_concurrent_log": {
                "level": "DEBUG",
                "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                # Example of a custom format for this log.
                "formatter": "example2",
                # 'formatter': 'default',
                "filename": log_name,
                # Optional: set an owner and group for the log file
                # 'owner': ['greenfrog', 'admin'],
                # Sets permissions to owner and group read+write
                "chmod": 0o0660,
                # Note: this is abnormally small to make it easier to demonstrate rollover.
                # A more reasonable value might be 10 MiB or 10485760
                "maxBytes": 240,
                # Number of rollover files to keep
                "backupCount": 10,
                # 'use_gzip': True,
            }
        },
        # Tell root logger to use our concurrent handler
        "root": {
            "handlers": ["my_concurrent_log"],
            "level": "DEBUG",
        },
    }

    logging.config.dictConfig(logging_config)


if __name__ == "__main__":
    my_program()
