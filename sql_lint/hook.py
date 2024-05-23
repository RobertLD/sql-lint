import argparse
import fnmatch
from typing import Sequence

import importlib_resources
from sqlfluff.core.config import FluffConfig

from sql_lint.sql_formatter import SQLFormatter


def main(argv: Sequence[str] | None = None):
    args = process_arguments(argv)

    sql_files = fnmatch.filter(args.files, args.file_pattern)
    if not sql_files:
        return
    if not args.config:
        config = FluffConfig.from_string(
            importlib_resources.read_text("sql_lint", ".sqlfluff")
        )
    else:
        config = FluffConfig.from_path(args.config)

    edit_inplace = True if not args.lint else False

    SQLFormatter(sql_files, edit_inplace, config).format_all()


def process_arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Filenames to lint/fix")
    parser.add_argument(
        "-f",
        "--file_pattern",
        default="*.sql",
        help="Match files containing pattern (glob syntax)",
    )
    parser.add_argument(
        "-c", "--config", help="Path to SQLFluff compatible config file"
    )
    parser.add_argument("-l", "--lint", help="Lint files, but do not fix")
    args = parser.parse_args(argv)
    return args
