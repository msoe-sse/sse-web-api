# Setup
1. You will need python installed on your development machine.
    - Check version with python --version
2. Ask the webmaster for the credentials.json, the API key for this service, and the development google file id
3. Clone the repository
4. Navigate to your project directory in git bash
5. Run `pip install -r requirements.txt`
6. Place the credentials.json in your project directory and run `export GOOGLE_APPLICATION_CREDENTIALS="$(< credentials.json)"`
7. Run `export API_KEY="<API Key Here>"`
8. Run `export GOOGLE_FILE_ID="<File Id Here>"`
8. To check that the environment variables have been applied correctly run `echo $GOOGLE_APPLICATION_CREDENTIALS`, `echo $API_KEY`, and `echo $GOOGLE_FILE_ID`
9. To run the service locally run `python main.py` and navigate to http://127.0.0.1:5000/points?source=<> in your prefered browser or test the response using a program like postman
    - The source parameter is either drive or sheets corresponding to Google Drive or Gooogle Sheets
