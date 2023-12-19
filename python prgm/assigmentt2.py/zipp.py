import zipfile
with zipfile.ZipFile('C:/Users/DELL/Desktop/python prgm/assigmentt2.py/example.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')

import zipfile
with zipfile.ZipFile('C:/Users/DELL/Desktop/python prgm/assigmentt2.py/example.zip','r') as zipfile:
    file_list=zipfile.namelist()
    print("contents of the zipfile",file_list)
