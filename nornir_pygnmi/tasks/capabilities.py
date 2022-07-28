"""This module contains the Nornir task for GNMI Capabilities() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def gnmi_capabilities(task: Task) -> Result:
    """This task is based on Capabilites() GNMI RPC.
    The RPC takes no inputs and reutrns dictionary of supported by a device capabilities.
    However, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    gnmi_conn = task.host.get_connection(connection="pygnmi", configuration=task.nornir.config)

    result = gnmi_conn.capabilities()

    return Result(host=task.host, result=result, changed=False)
