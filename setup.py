#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, Command


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
        os.system("black .".format(sys.executable))
        sys.exit()


# Where the magic happens:
setup(
    cmdclass={
        "format": FormatCommand,
    },
)
