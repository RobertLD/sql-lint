"""Constants and reusable definitions."""

from enum import StrEnum


class FileOpenMode(StrEnum):
    """Available file opening modes."""

    READ = "r"
    WRITE = "w"
    APPEND = "a"


class TextCase(StrEnum):
    """Valid casing options."""

    UPPER = "upper"
    LOWER = "lower"
    PASCAL = "capitalize"


class OSLineEndings(StrEnum):
    """Available line-endings for each OS."""

    WINDOWS = "\r\n"
    UNIX = "\n"
