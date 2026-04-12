# If you receive a message error not allowing to run the script setup.ps1, copy and paste next command in PowerShell --> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

cd..
# Windows usually uses 'python' or 'py' instead of 'python3.12'
python -m venv .adk_env

# Activate the virtual environment in PowerShell
.\.adk_env\Scripts\Activate.ps1

python --version
pip install -r requirements.txt

# Create the multiline string and output it to .env
$envText = @"
# Take out next 2 comments to use Gemini API key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here

# Take out next 3 comments to use Vertex AI
#GOOGLE_CLOUD_PROJECT="GCP_PROJECT_ID"
#GOOGLE_CLOUD_LOCATION="europe-west1" # e.g., us-central1
#GOOGLE_GENAI_USE_VERTEXAI=TRUE
#gcloud auth application-default login --> use previous command in the terminal to authenticate only once
#gcloud auth application-default revoke --> for logout from previous ADC login
"@

Add-Content -Path .\.env -Value $envText -Encoding UTF8

adk --version

Write-Host "All installed, try to run the next command for checking all is ok: --> adk --version"
Write-Host "Update the .env file in the current folder with your API KEY, then move into scripts folder and run copyKey.ps1"