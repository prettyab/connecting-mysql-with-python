# import zipfile
# with zipfile.ZipFile("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/file.zip","r") as zipfile:
#     file_list=zipfile.namelist()
#     print("contents of the zipfile",file_list)

# import zipfile
# with zipfile.ZipFile("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/file.zip","w") as zipfile:
#     zipfile.write("file1.txt")
#     zipfile.write("file2.txt")

# EXTRACTION

# import zipfile
# file_to_extract='file1.txt'
# extraction_path="C:/Users/DELL/Documents"
# with zipfile.ZipFile('example.zip','r') as zipf:
#     if file_to_extract in zipf.namelist():
#         zipf.extract(file_to_extract,extraction_path)
#         print(f"'{file_to_extract}'to been extracted to '{extraction_path}'.")
#     else:
#         print(f"'{file_to_extract}'does not exist in the ZIP achieve.")

