"""This module contains the Nornir task for GNMI Get() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def gnmi_get(task: Task, prefix: str = "", path: list = None,
             target: str = None, datatype: str = 'all',
             encoding: str = 'json') -> Result:
    """This task is based on Get() GNMI RPC.
    The RPC takes a number of inputs and reutrns dictionary of supported by a device capabilities.
    Also, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    gnmi_conn = task.host.get_connection(connection="pygnmi", configuration=task.nornir.config)
    gnmi_conn.capabilities()

    result = gnmi_conn.get(prefix=prefix,
                           path=path,
                           target=target,
                           datatype=datatype,
                           encoding=encoding)

    return Result(host=task.host, result=result, changed=False)
