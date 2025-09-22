import os
import re

# Get all files in current directory
for filename in os.listdir('.'):
    # Only process files (skip directories)
    if os.path.isfile(filename):
        # Replace '+-+' or '++-' with a space first, then single '+'
        new_name = re.sub(r'\+\-+|\+\+', ' ', filename)
        new_name = new_name.replace('+', ' ')
        
        # Rename the file if the name changed
        if new_name != filename:
            print(f"Renaming:\n  {filename} -> {new_name}")
            os.rename(filename, new_name)
