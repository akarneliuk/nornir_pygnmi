"""This file contains simple path for all GNMI tasks leveraging pygnmi"""
# Modules
from nornir_pygnmi.tasks.capabilities import gnmi_capabilities
from nornir_pygnmi.tasks.get import gnmi_get


# Variables
__all__ = (
    "gnmi_capabilities",
    "gnmi_get"
)
