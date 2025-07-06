import os
import re

# Precompile the regex pattern for efficiency
pattern = re.compile(r'(\d+)\s+0\s+obj\s')

# List and process each .bin file in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        with open(filename, 'rb') as f:
            data = f.read()
        
        clean_bytes = bytearray()
        for byte in data:
            if byte in (9, 10, 13, 32):  # Tab, LF, CR, Space
                clean_bytes.append(32)     # Convert to space
            elif 48 <= byte <= 57:        # Digits 0-9
                clean_bytes.append(byte)
            elif 33 <= byte <= 126: # ASCII printable characters
                clean_bytes.append(byte)
            else:
                clean_bytes.append(32)     # Replace other bytes with space
        
        text = clean_bytes.decode('ascii', errors='ignore').lower()
        
        # Find all matches in the cleaned text
        matches = pattern.findall(text)
        if matches:
            first_num = matches[0]
            last_num = matches[-1]
        else:
            first_num = 'N/A'
            last_num = 'N/A'
        
        print(f"{filename}, {first_num}, {last_num}")