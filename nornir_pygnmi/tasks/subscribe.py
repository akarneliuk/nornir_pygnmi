"""This module contains the Nornir task for GNMI Subscribe() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def gnmi_subscribe(task: Task) -> Result:
    """This task is based on Subscribe() GNMI RPC.
    The RPC takes a number of inputs and reutrns dictionary of supported by a device capabilities.
    Also, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    raise NotImplementedError
    gnmi_conn = task.host.get_connection(connection="pygnmi", configuration=task.nornir.config)
