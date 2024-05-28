Pre-commit SQL Linter/Fixer
===============================

This is a [pre-commit](https://github.com/pre-commit) hook that lint and fix your SQL files
utilizing SQLFluff

* [pre-commit](https://github.com/pre-commit)
* [sqlfluff](https://sqlfluff.com/)


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git@github.com:RobertLD/sql-lint.git
      sha: 0.0.1
      hooks:
      - id: sql-lint
        args: ['--file_pattern', '*.sql']

Available flags:

* ``--lint``: Lint but do not automatically fix files
* ``--config``: File path for SQLfluff config file
* ``--file_pattern``: File pattern to match staged files against (glob syntax)

The hook supports [sqlfluff's configuration files](https://docs.sqlfluff.com/en/stable/configuration.html) - Please refer to the sqlfluff documentation for reference
