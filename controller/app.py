from flask import Flask

from selenium_context import SeleniumContext

app = Flask(__name__)


@app.route('/')
def hello_world():
    slnm = SeleniumContext.get_instance()
    slnm.login()
    slnm.navigate_to_active_sprint_board()
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
