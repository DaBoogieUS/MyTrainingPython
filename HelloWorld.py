import os
ext = 'ED '
path = 'C://Users/Nicolas Jackson/OneDrive - tdsgroup.biz/Knowledges/Peter/Engineering Drawings/Engineering Drawings/Various/'

print(os.listdir(path))
min
for file in os.listdir(path):
    if file[0:3] != ext:
        os.rename(path+file, path+ext+file)
    else:
        print("Already renamed!")