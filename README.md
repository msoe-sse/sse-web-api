# Setup
1. You will need python installed on your development machine.
    - Check version with python --version
2. Clone the repository
3. Navigate to your project directory in git bash
4. Run `pip install virtualenv` and then `virtualenv env`
5. Activate your virtualenv by running `./env/Scripts/activate`
6. Install the dependencies for this project by running `./env/Scripts/pip install -r requirements.txt`
7. Follow the specific setup steps below depending on which endpoints you're working on.
8. To run the service locally run `./scripts/debug.sh` and navigate to http://localhost:5000 in your preferred browseer and follow the API documentation to call a various endpoint.
9. To run all unit tests run `./scripts/test.sh`

# Setup needed for testing SSE Points endpoints
1. Ask the webmaster for the credentials.json, the API key for google sheets, and the development google file id
2. Place the credentials.json in your project directory and run `export GOOGLE_APPLICATION_CREDENTIALS="$(< credentials.json)"`
3. Run `export API_KEY="<API Key Here>"`
4. Run `export GOOGLE_FILE_ID="<File Id Here>"`
5. To check that the environment variables have been applied correctly run `echo $GOOGLE_APPLICATION_CREDENTIALS`, `echo $API_KEY`, and `echo $GOOGLE_FILE_ID`

# Setup needed for testing SSE Resources endpoints
1. Ask the webmaster for the Airtable API key.
2. Run `export AIRTABLE_API_KEY="<API Key Here>"`
3. Run `export RESOURCE_TABLE="ResourcesStaging"`
