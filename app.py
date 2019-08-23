from flask import Flask
from jira import JIRA

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()

    jac = JIRA('https://jira.atlassian.com')

    jira = JIRA(options={
        'server': 'https://poulad.atlassian.net',
        'basic_auth': ('poulad', 'pass')
    })
    iss = jira.issue(1)
    pass
