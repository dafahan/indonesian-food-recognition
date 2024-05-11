import os

# List to store directory names
directories = []

# Iterate over the directories in the train directory
for dirname, _, _ in os.walk('/home/dafahan/Downloads/makanan/train'):
    # Extract the directory name from the path
    directory_name = os.path.basename(dirname)
    # Append the directory name to the list
    directories.append(directory_name)

# Print the list of directory names
print("Directories in the train directory:",end=" ")
# Print the directory names using their index
print("labels = {")
for i in range(len(directories)):
    if i == 0 :
        continue

    print(f"{i-1}: '{directories[i]}'",end=" , ")

print("}")
