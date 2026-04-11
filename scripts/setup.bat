cd..
mkdir IE-GDG-ADK
cd IE-GDG-ADK

:: Windows usually uses 'python' or 'py' instead of 'python3.12'
python -m venv .adk_env

:: Activate the virtual environment in CMD
call .adk_env\Scripts\activate.bat

python --version
pip install -r ..\requirements.txt
adk --version

:: Create and append to the .env file line by line
echo # Take out next 2 comments to use Gemini API key > .env
echo GOOGLE_GENAI_USE_VERTEXAI=FALSE >> .env
echo GOOGLE_API_KEY=your_api_key_here >> .env
echo. >> .env
echo # Take out next 3 comments to use Vertex AI >> .env
echo #GOOGLE_CLOUD_PROJECT="GCP_PROJECT_ID" >> .env
echo #GOOGLE_CLOUD_LOCATION="europe-west1" # e.g., us-central1 >> .env
echo #GOOGLE_GENAI_USE_VERTEXAI=TRUE >> .env
echo #gcloud auth application-default login --^> use previous command in the terminal to authenticate only once >> .env
echo #gcloud auth application-default revoke --^> for logout from previous ADC login >> .env