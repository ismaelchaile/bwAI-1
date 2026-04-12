# Adds the .env file inside each agent folder with an api key and all changes you made.

# Safely move to the parent directory. If it fails, the script stops.
cd .. || { echo "Failed to change directory"; exit 1; }

# 1. Define the file to be copied and the parent folder
SOURCE_FILE=".env"
# Removed the trailing slash here so we can format the path cleanly below
AGENTS_PARENT_FOLDER="agents" 

# 2. Check if the source file actually exists before starting
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' does not exist in the root directory. Run ./setup.sh first"
    exit 1
fi

# 3. Check if the parent folder actually exists
if [ ! -d "$AGENTS_PARENT_FOLDER" ]; then
    echo "Error: Parent folder '$AGENTS_PARENT_FOLDER' does not exist."
    exit 1
fi

# 4. Loop dynamically through all non-hidden directories inside the parent folder
# The '/*/' at the end of the variable ensures we ONLY match directories.
# By default, bash ignores hidden directories (like .git or .vscode) when using '*'.
for folder_path in "$AGENTS_PARENT_FOLDER"/*/; do
    
    # Safety check: if no directories exist, the glob might just return the literal string. 
    # This prevents the script from trying to copy into a folder named literally "agents/*/"
    if [ -d "$folder_path" ]; then
        cp "$SOURCE_FILE" "$folder_path"
        echo "✅ $SOURCE_FILE copied to: $folder_path"
    fi

done

echo "🎉 All copy operations complete!"