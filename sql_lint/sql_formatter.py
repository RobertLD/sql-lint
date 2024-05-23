from pathlib import Path

import sqlfluff
from sqlfluff.core.config import FluffConfig

from sql_lint.utils import FileOpenMode


class SQLFormatter:
    """Open file and preform SQL formatting operations as configured"""

    def __init__(
        self,
        file_paths: list[Path] | Path,
        edit_inplace: bool,
        fluff_config: FluffConfig,
    ):
        if not isinstance(file_paths, list):
            file_paths = [file_paths]
        self.file_paths = file_paths

        self.edit_inplace = edit_inplace
        self.config = fluff_config

    def _sql_transform(self, file_path: Path) -> str | None:
        if self.edit_inplace:
            with open(file_path, FileOpenMode.READ) as sql_file:
                sql_fstr = sql_file.read()
            with open(file_path, FileOpenMode.WRITE) as sql_file:
                if linted_sql := sqlfluff.fix(sql_fstr, config=self.config):
                    sql_file.write(linted_sql)
            return None
        else:
            with open(file_path, FileOpenMode.READ) as sql_file:
                sql_fstr = sql_file.read()
            return sqlfluff.fix(sql_fstr, config=self.config)

    def format_all(self):
        output = []
        for file_path in self.file_paths:
            formatted_sql = self._sql_transform(file_path)
            if formatted_sql is not None:
                output += formatted_sql
        return output
