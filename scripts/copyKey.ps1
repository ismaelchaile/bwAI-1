# Adds the .env file inside each agent folder with an api key and all changes you made.

# Safely move to the parent directory.
Set-Location .. -ErrorAction Stop

# 1. Define the file to be copied and the parent folder
$SourceFile = ".env"
$AgentsParentFolder = "agents"

# 2. Check if the source file actually exists before starting
if (-Not (Test-Path -Path $SourceFile -PathType Leaf)) {
    Write-Error "Error: '$SourceFile' does not exist in the root directory. Run setup.ps1 first."
    exit
}

# 3. Check if the parent folder actually exists
if (-Not (Test-Path -Path $AgentsParentFolder -PathType Container)) {
    Write-Error "Error: Parent folder '$AgentsParentFolder' does not exist."
    exit
}

# 4. Loop dynamically through all directories inside the parent folder
# Get-ChildItem with -Directory only fetches folders. 
# Without the -Force switch, it naturally ignores hidden folders.
$targetFolders = Get-ChildItem -Path $AgentsParentFolder -Directory

foreach ($folder in $targetFolders) {
    # Copy the file to the destination
    Copy-Item -Path $SourceFile -Destination $folder.FullName -Force
    Write-Host "✅ $SourceFile copied to: $($folder.FullName)" -ForegroundColor Green
}

Write-Host "🎉 All copy operations complete!" -ForegroundColor Cyan