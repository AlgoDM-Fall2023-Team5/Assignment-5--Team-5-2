import os
import shutil


original_folder = "C:/Users/shiri/Documents/Assg5ADM/Assignment-5--Team-5/dataset"
new_folder = "C:/Users/shiri/Documents/Assg5ADM/Assignment-5--Team-5/new_dataset"

# Create the new folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

count = 0
for root, dirs, files in os.walk(original_folder):
    for file in files:
        # Check if "front" is in the file name
        if "front" in file.lower() and file.endswith(".jpg"):
            # Create the full paths for the original and new files
            original_path = os.path.join(root, file)
            new_path = os.path.join(new_folder, file)
            
            # Copy the file to the new folder
            shutil.copyfile(original_path, new_path)
            
            #print(f"File '{file}' copied to '{new_folder}'")
            count = count+1
        
print(count)

print("Process completed.")
