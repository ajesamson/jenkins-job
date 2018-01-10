# Jenkins Job

A script, in Python, that uses Jenkins' API to get a list of jobs and 
their status from a given Jenkins instance. The status for each job 
are stored in a sqlite database along with the time for when it was
 checked.

## Usage

Following the following process to run the python script

1. Clone repo and change directory to the project folder from 
any suitable terminal

2. Start virtual environment
    ```text
      source bin/activate
    ```
    
3. Create a `.env` file and provide the following environment variable
    ```text
       JENKINS_SERVER=Jenkins server address such as ci.cgi.org:8080
       JENKINS_USER=Valid username
       JENKINS_TOKEN=Token provided for user
    ```
    
    Note: The Jenkins server address should be without `http://`

4. Run the application
    ```text
    python app.py
    ```

5. In order to view the record, use an [sqlite browser](http://sqlitebrowser.org/)
   to open the generated `data.db` file in the project directory
   
6. To exist from the terminal, enter `deactivate` and press enter to exit
    