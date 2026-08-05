"""A monochrome icon set for novelibre.

Requires Python 3.7+
Copyright (c) Peter Triesberger
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
from pathlib import Path
import shutil


class Plugin:
    """Icon set plugin class."""
    VERSION = '@release'
    API_VERSION = '5.63'
    DESCRIPTION = 'Monochrome icon set'
    URL = 'https://github.com/peter88213/nv_bw_icons'
    HELP_SITE = 'https://peter88213.github.io/nv_bw_icons'
    HELP_PAGE = 'help'

    def install(self, model, view, controller):
        """Install the plugin at runtime."""
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

        self._add_help_menu_entry('nv_bw_icons plugin help')

    def uninstall(self):
        if self.iconPath is not None:
            shutil.rmtree(self.iconPath, ignore_errors=True)
            self.iconPath = None

