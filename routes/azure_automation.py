from flask import render_template

from .azure_automation_data.quickstarts import azure_quickstarts
from .azure_automation_data.application_workloads import azure_application_workloads


def azure_quickstarts_route():
    return render_template(
        "azure/quickstarts.html",
        azure_templates=azure_quickstarts,

    )


def azure_quickstarts_action_route(azure_action):
    actions = azure_quickstarts[azure_action]
    return render_template(
        "azure/quickstarts.html",
        azure_action=azure_action,
        azure_templates=azure_quickstarts,
        actions=actions,
    )


def azure_application_workloads_route():
    return render_template(
        "azure/application_workloads.html",
        azure_templates=azure_application_workloads,
    )


def azure_application_workloads_action_route(azure_action):
    actions = azure_application_workloads[azure_action]
    return render_template(
        "azure/application_workloads.html",
        azure_action=azure_action,
        azure_templates=azure_application_workloads,
        actions=actions,
    )
