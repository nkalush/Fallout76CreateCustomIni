""" This module creates a fallout76Custom.ini file from the installed mods in the data directory """

import os
from os import walk

# Get the home directory of the current user
HOME_DIR = os.path.expanduser("~") + "\\Documents\\My Games\\Fallout 76\\fallout76Custom_test.ini"

# Open the Custom.ini file for writing
CUSTOM_INI_FILE = open(HOME_DIR, "w+")

# write the section header to the file
CUSTOM_INI_FILE.write("[Archive]\r\n")

# Configuration arrays, these are mods that should go in specific
# lists, all other go in sResourceArchive2List
STARTUP_MODS = ['IconTag.ba2']
FILE_LIST_MODS = ['UHDmap.ba2']
LIST2_MODS = ['SaveMyStuff.ba2']
SR_STARTUP_LIST = []
SR_INDEX_FILE_LIST = []
SR_ARCHIVE_LIST2 = []
SR_ARCHIVE_2LIST = []

for (dirpath, dirnames, filenames) in walk('data'):
    for file in filenames:
        if (file[0:10] != 'SeventySix' and file[-4:] == '.ba2'):
            if file in STARTUP_MODS:
                SR_STARTUP_LIST.append(file)
            elif file in FILE_LIST_MODS:
                SR_INDEX_FILE_LIST.append(file)
            elif file in LIST2_MODS:
                SR_ARCHIVE_LIST2.append(file)
            else:
                SR_ARCHIVE_2LIST.append(file)
    break

if SR_STARTUP_LIST:
    SR_STARTUP_DEFAULTS = [
        'SeventySix - Interface.ba2',
        'SeventySix - Localization.ba2',
        'SeventySix - Shaders.ba2',
        'SeventySix - Startup.ba2'
        ]
    SR_STARTUP_LIST = SR_STARTUP_DEFAULTS + SR_STARTUP_LIST
    CUSTOM_INI_FILE.write("sResourceStartUpArchiveList = %s\r\n" % ', '.join(SR_STARTUP_LIST))

if SR_ARCHIVE_LIST2:
    SR_ARCHIVE_LIST2_DEFAULTS = [
        'SeventySix - Animations.ba2',
        'SeventySix - EnlightenInteriors.ba2',
        'SeventySix - GeneratedTextures.ba2',
        'SeventySix - EnlightenExteriors01.ba2',
        'SeventySix - EnlightenExteriors02.ba2'
        ]
    SR_ARCHIVE_LIST2 = SR_ARCHIVE_LIST2_DEFAULTS + SR_ARCHIVE_LIST2
    CUSTOM_INI_FILE.write("sResourceArchiveList2 = %s\r\n" % ', '.join(SR_ARCHIVE_LIST2))

if SR_INDEX_FILE_LIST:
    SR_FILE_LIST_DEFAULTS = [
        'SeventySix - Textures01.ba2',
        'SeventySix - Textures02.ba2',
        'SeventySix - Textures03.ba2',
        'SeventySix - Textures04.ba2',
        'SeventySix - Textures05.ba2',
        'SeventySix - Textures06.ba2'
        ]
    SR_INDEX_FILE_LIST = SR_FILE_LIST_DEFAULTS + SR_INDEX_FILE_LIST
    CUSTOM_INI_FILE.write("sResourceIndexFileList = %s\r\n" % ', '.join(SR_INDEX_FILE_LIST))

if SR_ARCHIVE_2LIST:
    SE_2LIST_DEFAULTS = [
        'SeventySix - ATX_Main.ba2',
        'SeventySix - ATX_Textures.ba2'
        ]
    SR_ARCHIVE_2LIST = SE_2LIST_DEFAULTS + SR_ARCHIVE_2LIST
    CUSTOM_INI_FILE.write("sResourceArchive2List = %s\r\n" % ', '.join(SR_ARCHIVE_2LIST))

CUSTOM_INI_FILE.close()
