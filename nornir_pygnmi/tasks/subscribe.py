"""This module contains the Nornir task for GNMI Subscribe() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def gnmi_subscribe(task: Task, subscribe: dict, 
                   target: str = None, extension: list = None) -> Result:
    """This task is based on Subscribe() GNMI RPC.
    The RPC takes a number of inputs and reutrns dictionary of supported by a device capabilities.
    Also, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    gnmi_conn = task.host.get_connection(connection="pygnmi", configuration=task.nornir.config)
    gnmi_conn.capabilities()

    result = []

    for item in gnmi_conn.subscribe2(subscribe=subscribe,
                                     target=target,
                                     extension=extension):
        result.append(item)

    return Result(host=task.host, result=result, changed=False)
