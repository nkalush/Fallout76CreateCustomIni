import os
from os import walk

# Get the home directory of the current user
homeDir = os.path.expanduser("~")

# Open the Custom.ini file for writing
f = open(homeDir + "\\Documents\\My Games\\Fallout 76\\fallout76Custom.ini","w+")

# write the section header to the file
f.write("[Archive]\r\n")

# this refers to the data folder where mods are located
mypath = 'data'

skipfiles = ['__folder_managed_by_vortex', 'vortex.deployment.json']
startupMods = ['IconTag.ba2']
fileListMods = ['UHDmap.ba2']
list2Mods = ['SaveMyStuff.ba2']
sResourceStartUpArchiveList = []
sResourceIndexFileList = []
sResourceArchiveList2 = []
sResourceArchive2List = []

for (dirpath, dirnames, filenames) in walk(mypath):
	for file in filenames:
		#if (file[0:10] != 'SeventySix' and file not in skipfiles):
		if (file[0:10] != 'SeventySix' and file[-4:] == '.ba2'):
			if (file in startupMods):
				sResourceStartUpArchiveList.append(file)
			elif  (file in fileListMods):
				sResourceIndexFileList.append(file)
			elif  (file in list2Mods):
				sResourceArchiveList2.append(file)
			else:
				sResourceArchive2List.append(file)
	break

if (len(sResourceStartUpArchiveList) > 0):
	for file in ['SeventySix - Interface.ba2', 'SeventySix - Localization.ba2', 'SeventySix - Shaders.ba2', 'SeventySix - Startup.ba2']:
		sResourceStartUpArchiveList.insert(0, file)
	f.write("sResourceStartUpArchiveList = %s\r\n" % ', '.join(sResourceStartUpArchiveList))

if (len(sResourceArchiveList2) > 0):
	for file in ['SeventySix - Animations.ba2', 'SeventySix - EnlightenInteriors.ba2', 'SeventySix - GeneratedTextures.ba2', 'SeventySix - EnlightenExteriors01.ba2', 'SeventySix - EnlightenExteriors02.ba2']:
		sResourceArchiveList2.insert(0, file)
	f.write("sResourceArchiveList2 = %s\r\n" % ', '.join(sResourceArchiveList2))

if (len(sResourceIndexFileList) > 0):
	for file in ['SeventySix - Textures01.ba2', 'SeventySix - Textures02.ba2', 'SeventySix - Textures03.ba2', 'SeventySix - Textures04.ba2', 'SeventySix - Textures05.ba2', 'SeventySix - Textures06.ba2']:
		sResourceIndexFileList.insert(0, file)
	f.write("sResourceIndexFileList = %s\r\n" % ', '.join(sResourceIndexFileList))

if (len(sResourceArchive2List) > 0):
	for file in ['SeventySix - ATX_Main.ba2', 'SeventySix - ATX_Textures.ba2']:
		sResourceArchive2List.insert(0, file)
	f.write("sResourceArchive2List = %s\r\n" % ', '.join(sResourceArchive2List))

f.close()
