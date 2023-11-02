from flask import Flask

from routes import (
    index,
    azure_automation
)

azure_automation_tool = Flask(__name__)

azure_automation_tool.secret_key = 'super secret key'
azure_automation_tool.config['SESSION_TYPE'] = 'filesystem'
azure_automation_tool.add_url_rule('/', view_func=index.index_route)
azure_automation_tool.add_url_rule('/index.html', view_func=index.index_route)
azure_automation_tool.add_url_rule('/azure/quickstarts', view_func=azure_automation.azure_quickstarts_route)
azure_automation_tool.add_url_rule('/azure/quickstarts/actions/<string:azure_action>', view_func=azure_automation.azure_quickstarts_action_route)
azure_automation_tool.add_url_rule('/azure/application_workloads', view_func=azure_automation.azure_application_workloads_route)
azure_automation_tool.add_url_rule('/azure/application_workloads/actions/<string:azure_action>', view_func=azure_automation.azure_application_workloads_action_route)


if __name__ == '__main__':
    azure_automation_tool.run(debug=True)
