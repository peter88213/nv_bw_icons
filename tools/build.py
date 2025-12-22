"""Build the nv_bw_icons novelibre plugin package.
        
Note: VERSION must be updated manually before starting this script.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_bw_icons
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copytree
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '5.1.0'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_bw_icons'
    LOCAL_LIB = 'nvplugin'
    GERMAN_TRANSLATION = False

    def add_icons(self):
        copytree('../nv_bw_icons', f'{self.buildDir}/nv_bw_icons')

    def add_extras(self):
        self.add_icons()


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()
