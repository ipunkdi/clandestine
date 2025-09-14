"""JSON logger utility for structured logging."""

import logging
import json
from pathlib import Path


class JsonFormatter(logging.Formatter):
    """Custom logging formatter to output logs as JSON."""

    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
        }
        return json.dumps(log_record)


def setup_logger(name: str, log_file: Path, level: str = "INFO") -> logging.Logger:
    """
    Setup a logger that writes JSON formatted logs to a file.

    Args:
        name (str): Logger name.
        log_file (Path): Path to log file.
        level (str): Logging level, e.g., "DEBUG", "INFO", "WARNING".

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level.upper())

    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(JsonFormatter())

    # Hindari duplikasi handler saat dipanggil berkali-kali
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
