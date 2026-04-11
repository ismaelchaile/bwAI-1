cd ..
python3.12 -m venv .adk_env
source .adk_env/bin/activate
python --version
pip install -r requirements.txt
adk --version
echo  '
# Take out next 2 comments to use Gemini API key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here

# Take out next 3 comments to use Vertex AI
#GOOGLE_CLOUD_PROJECT="GCP_PROJECT_ID"
#GOOGLE_CLOUD_LOCATION="europe-west1" # e.g., us-central1
#GOOGLE_GENAI_USE_VERTEXAI=TRUE
#gcloud auth application-default login --> use previous command in the terminal to authenticate only once
#gcloud auth application-default revoke --> for logout from previous ADC login' >> ./.env