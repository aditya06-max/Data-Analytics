import os  #The os module helps Python interact with the operating system

import shutil  #This module is used for high-level file operations.

#Folder path you want to organise 
FOLDER_PATH = os.getcwd()  #Current working directory 

#File type mapping
FILE_TYPES ={
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Documents': ['.pdf','.docx','.doc','.txt','.xlsx','.pptx','.md'],
    'Audio': ['.mp3','.wav','.aac','.flac'],
    'Videos': ['.mp4','.avi','.mov','.mkv'],
    'Archives': ['.zip','.rar','.tar','.gz'],
    'Scripts': ['.js','.sh','.bat'],
}

#Create folders if they don't exist
for folder in FILE_TYPES.keys(): #Create folder for each file type
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path): #if folder path does not exist then make one.
        os.makedirs(folder_path)

#Oraganize files
for file in os.listdir(FOLDER_PATH): #os.listdir Returns everything inside the folder.
    file_path = os.path.join(FOLDER_PATH , file)

    #Skip folders
    if os.path.isdir(file_path): #This is function which checks whether this file is folder or not.
        continue

    #Get file extensions
   # print(os.path.splitext(file))
    file_ext = os.path.splitext(file)[1].lower()
    #  Explaination of this line 
    # Suppose:

# file = "cat.jpg"

# Then:

# os.path.splitext(file)

# returns:

# ('cat', '.jpg')
# Step 2
# [1]

# takes the second part:

# '.jpg'
# Step 3
# .lower()

# converts uppercase to lowercase.

# Example:

# .JPG

# becomes:

# .jpg

# So matching becomes easier.

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder,file))

print("Files organised succesfully✅")            
