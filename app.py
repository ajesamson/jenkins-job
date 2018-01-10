import os
import jenkins
from os.path import join, dirname
from dotenv import load_dotenv

from status_table import DbManagement

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ci_server = os.getenv('JENKINS_SERVER')
ci_user = os.getenv('JENKINS_USER')
ci_token = os.getenv('JENKINS_TOKEN')

try:
    # initialize the database table it is not existing
    dbManagement = DbManagement()
    dbManagement.setup_table()
    # create jenkins instance
    server = jenkins.Jenkins(ci_server, username=ci_user, password=ci_token)

    # retrieve the jobs
    jobs = server.get_jobs()
    job_status = []
    for job in jobs:
        current_job = (job['name'], job['color'])
        job_status.append(current_job)

    if len(job_status):
        dbManagement.insert_status(job_status)

    print("Jenkins instance jobs saved to db successfully")
except:
    print("Jenkins job status logging process failed")
