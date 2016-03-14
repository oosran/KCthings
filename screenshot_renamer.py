# Tiny script to rename files from the standard KC3 screenshot name format to something more familiar to users of KCV.
# There is absolutely no need to do this, but personally I prefer the KCV format to KC3's.
# That's literally the only reason I made this in the first place.
#
# Couple things that can be easily modified:
# -uncomment lines 18 and/or 26 to get printouts of source/destination directories and old_name->new_name
# -comment line 30 if you're using the same source and destination folders as it's not necessary in that case
# -if for some reason you have jpeg screenshots change the if on line 22 to either include .jpg or replace .png completely

from os import rename, listdir
import shutil

print("Remember to set the directories first! (And then you can comment out this print)")
"""
src = "C:\\Path\\To\\Source\\Folder\\"
dst = "D:\\Path\\To\\Destination\\Folder\\"

#print("src="+src+"\ndst="+dst)

#for fname in listdir('.'):
for fname in listdir(src):
	if "[" in fname and ".png" in fname:
		split_name = fname.split(" ", 1)
		badprefix, new_name = split_name[0], "KanColle-"+split_name[1].replace("20","").replace('-','').replace(' ','-',1).replace(' ','')

		#print("Renaming: \""+fname+"\" to: \""+new_name+"\"")

		rename(fname, new_name)

		shutil.move(src+new_name, dst+new_name)
	else: pass
"""