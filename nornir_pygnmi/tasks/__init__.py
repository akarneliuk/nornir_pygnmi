"""This file contains simple path for all GNMI tasks leveraging pygnmi"""
# Modules
from nornir_pygnmi.tasks.capabilities import gnmi_capabilities
from nornir_pygnmi.tasks.get import gnmi_get
from nornir_pygnmi.tasks.set import gnmi_set
from nornir_pygnmi.tasks.subscribe import gnmi_subscribe


# Variables
__all__ = (
    "gnmi_capabilities",
    "gnmi_get",
    "gnmi_set",
    "gnmi_subscribe"
)
