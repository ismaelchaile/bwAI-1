:: Adds the .env file inside each agent folder with an api key and all changes you made.

@echo off
:: Safely move to the parent directory. If it fails, exit the script.
cd .. || exit /b 1

:: 1. Define the file to be copied and the parent folder
set "SOURCE_FILE=.env"
set "AGENTS_PARENT_FOLDER=agents"

:: 2. Check if the source file actually exists before starting
if not exist "%SOURCE_FILE%" (
    echo Error: '%SOURCE_FILE%' does not exist in the root directory. Run setup.bat first.
    exit /b 1
)

:: 3. Check if the parent folder actually exists
if not exist "%AGENTS_PARENT_FOLDER%\" (
    echo Error: Parent folder '%AGENTS_PARENT_FOLDER%' does not exist.
    exit /b 1
)

:: 4. Loop dynamically through all directories inside the parent folder
:: 'for /d' only matches directories. It naturally skips hidden folders.
for /d %%D in ("%AGENTS_PARENT_FOLDER%\*") do (
    :: copy /Y suppresses the overwrite prompt, >nul hides the "1 file(s) copied" message
    copy /Y "%SOURCE_FILE%" "%%D\" >nul
    echo %SOURCE_FILE% copied to: %%D
)

echo All copy operations complete!
pause