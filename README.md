# Downloads Folder Organizer

**Project Overview**

This Python script helps organize files in your Downloads folder by sorting them into designated subfolders based on their file type. The automation moves specific file types into categorized folders like "Pdf files," "Image files," "Text files," "Tuto files," and "APK files." The main goal is to keep the Downloads folder clean and organized.

**How It Works**

**1. Folder Creation:**
The script checks if folders for each file type (Pdf files, Image files, etc.) already exist. If not, it creates them in the Downloads directory.

**2. File Sorting:**

The script scans all files in the Downloads folder.
It moves files into their corresponding folders based on file extensions:
.pdf files go to the Pdf files folder.
.png files go to the Image files folder.
.txt files go to the Text files folder.
.mp4 files go to the Tuto files folder.
.exe files go to the APK files folder.
If a file doesn't match any of the specified types or is already in its respective folder, the script skips it.

Logging:

Files that don’t match the expected formats or folders are logged in the console.

**Completion:**
After processing all files, the script outputs "Operation completed successfully."

**4. Requirements**
Python 3.x
Libraries:
os: For interacting with the file system and folder paths.
shutil: To handle file movement operations.

**Installation and Setup**
Clone the repository or download the script.
Ensure Python 3 is installed on your system.
Edit the path variable in the script to point to your Downloads directory (if it's different from C:/Users/scale/Downloads/).
Run the script in your preferred Python environment.

**python organize_downloads.py**




# Customization

**Adding More File Types**: To organize additional file types, simply extend the elif conditions in the script to include the new file extensions and folder names.
Changing Folder Names: You can modify the folder names in the folder_names array to fit your preferences.
License
This project is open-source and available under the MIT License.

#Contributing
Feel free to submit issues or contribute improvements through pull requests.




