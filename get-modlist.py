# the script is written by chat-gpt because i don't know python

import os
import json
import zipfile

# Function to extract information from a fabric.mod.json file
def extract_mod_info(jar_file):
    mod_info = {"name": "", "version": "", "license": ""}
    
    with zipfile.ZipFile(jar_file, 'r') as jar:
        with jar.open('fabric.mod.json') as mod_json_file:
            mod_data = json.load(mod_json_file, strict=False)
            mod_info["name"] = mod_data.get("name", "")
            mod_info["version"] = mod_data.get("version", "")
            mod_info["license"] = mod_data.get("license", "")
            mod_info["environment"] = mod_data.get("environment", "")
    
    return mod_info

# Directory containing the .jar files
jar_directory = "./.minecraft/mods"

# Output file to store mod properties
output_file = "modlist.txt"

with open(output_file, 'w') as output:
    for root, dirs, files in os.walk(jar_directory):
        for file in files:
            if file.endswith(".jar"):
                jar_path = os.path.join(root, file)
                mod_info = extract_mod_info(jar_path)
                if mod_info["name"] and mod_info["version"]:
                    output.write(f"Name: {mod_info['name']}\n")
                    output.write(f"Version: {mod_info['version']}\n")
                    output.write(f"License: {mod_info['license']}\n")
                    output.write(f"Environment: {mod_info['environment']}\n")
                    output.write("\n")

print("Mod information extracted and saved to modlist.txt.")
