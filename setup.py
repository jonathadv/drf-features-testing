#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, Command

MODULE_NAMES = "tutorial snippets"


class LintCommand(Command):
    """Run pylint"""

    description = "Run pylint."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status("Running Pylint...")
        os.system(f"pipenv run pylint {MODULE_NAMES}".format(sys.executable))
        sys.exit()


class FormatCommand(Command):
    """Format code with Black"""

    description = "Format code with Black."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status("Formatting...")
        os.system("pipenv run black .".format(sys.executable))
        sys.exit()


# Where the magic happens:
setup(
    cmdclass={
        "format": FormatCommand,
        "lint": LintCommand,
    },
)
