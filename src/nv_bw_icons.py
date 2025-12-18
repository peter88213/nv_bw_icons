"""A "black/white" icon set for novelibre.

Requires Python 3.7+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_bw_icons
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import os
import shutil
from pathlib import Path


class Plugin:
    """Icon set plugin class."""
    VERSION = '@release'
    API_VERSION = '5.47'
    DESCRIPTION = 'Black/white icon set'
    URL = 'https://github.com/peter88213/nv_bw_icons'

    def install(self, model, view, controller):
        try:
            homeDir = str(Path.home()).replace('\\', '/')
            self.iconPath = f'{homeDir}/.novx/nv_bw_icons'
        except:
            self.iconPath = None
        if not os.path.isdir(self.iconPath):
            raise UserWarning(
                'Icons not found:'
                f'"{os.path.normpath(self.iconPath)}".'
            )

    def uninstall(self):
        if self.iconPath is not None:
            shutil.rmtree(self.iconPath, ignore_errors=True)
            self.iconPath = None

