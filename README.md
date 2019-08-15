# Setup
1. You will need python installed on your development machine.
    - Check version with python --version
2. Ask the webmaster for the credentials.json, the API key for this service, and the development google file id
3. Clone the repository
4. Navigate to your project directory in git bash
5. Run `pip install virtualenv` and then `virtualenv env`
6. Activate your virtualenv by running `./env/Scripts/activate`
7. Install the dependencies for this project by running `./env/Scripts/pip install -r requirements.txt`
6. Place the credentials.json in your project directory and run `export GOOGLE_APPLICATION_CREDENTIALS="$(< credentials.json)"`
7. Run `export API_KEY="<API Key Here>"`
8. Run `export GOOGLE_FILE_ID="<File Id Here>"`
8. To check that the environment variables have been applied correctly run `echo $GOOGLE_APPLICATION_CREDENTIALS`, `echo $API_KEY`, and `echo $GOOGLE_FILE_ID`
9. To run the service locally run `./scripts/debug.sh` and navigate to http://localhost:5000 in your preferred browseer and follow the API documentation to call a various endpoint.
10. To run all unit tests run `./scripts/test.sh`
