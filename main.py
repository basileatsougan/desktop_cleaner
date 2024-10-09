import os, shutil

 
# Define folder names on where we will move files
folder_names = ['Pdf files', 'Image files', 'Text files', 'Tuto files', 'APK files']

# Define path to 'Downloads' directory
path = r'C:/Users/scale/Downloads/'

# Create folders if they don't exist
for folder_name in folder_names:
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Get list of file names in 'Downloads' directory
file_names = os.listdir(path)

for file_name in file_names:
    file_path = os.path.join(path, file_name)
    if file_name.endswith('.pdf') and not os.path.exists(os.path.join(path, 'Pdf files', file_name)):
        shutil.move(file_path, os.path.join(path, 'Pdf files', file_name))
    elif file_name.endswith('.png') and not os.path.exists(os.path.join(path, 'Image files', file_name)):
        shutil.move(file_path, os.path.join(path, 'Image files', file_name))
    elif file_name.endswith('.txt') and not os.path.exists(os.path.join(path, 'Text files', file_name)):
        shutil.move(file_path, os.path.join(path, 'Text files', file_name))
    elif file_name.endswith('.mp4') and not os.path.exists(os.path.join(path, 'Tuto files', file_name)):
        shutil.move(file_path, os.path.join(path, 'Tuto files', file_name))
    elif file_name.endswith('.exe') and not os.path.exists(os.path.join(path, 'APK files', file_name)):
        shutil.move(file_path, os.path.join(path, 'APK files', file_name))
    else:
        if file_name not in folder_names:
            print(f"The file '{file_name}' was not moved.")
        
print("Operation completed succesfully.")
        
