"""This module contains the Nornir task for GNMI Set() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def gnmi_set(task: Task, delete: list = None, replace: list = None,
             update: list = None, encoding: str = 'json',
             prefix: str = "", target: str = None) -> Result:
    """This task is based on Set() GNMI RPC.
    The RPC takes a number of inputs and reutrns dictionary of supported by a device capabilities.
    Also, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    gnmi_conn = task.host.get_connection(connection="pygnmi", configuration=task.nornir.config)
    gnmi_conn.capabilities()

    result = gnmi_conn.set(delete=delete,
                           replace=replace,
                           update=update,
                           encoding=encoding,
                           prefix=prefix,
                           target=target)

    is_changed = True if result else False

    return Result(host=task.host, result=result, changed=is_changed)
