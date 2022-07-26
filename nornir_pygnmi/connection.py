"""This is a plugin to establish a long-living connectivity
to a network device via GNMI"""
# Modules
from typing import Optional, Any, Dict
from nornir.core.configuration import Config
from pygnmi.client import gNMIclient


# Classes
class PygnmiNornirConnectionPlugin:
    """This class creates a long-term connectivity to network device via GNMI
    using pyGNMI library"""

    def open(
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        port: Optional[int],
        platform: Optional[str],
        extras: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
    ) -> None:
        """Method to open the GNMI connectivity"""
        # Ditch variables which are not used at the moment
        _ = platform
        _ = configuration

        connection = gNMIclient(target=(hostname, port),
                                username=username,
                                password=password,
                                **extras)
        connection.connect()
        self.connection = connection

    def close(self) -> None:
        """Method to close the GNMI connectivity"""
        self.connection.close()
