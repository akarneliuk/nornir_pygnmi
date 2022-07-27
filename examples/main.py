"""Sample nornir_pygnmi script"""
# Modules
from nornir.init_nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pygnmi.tasks import gnmi_get, gnmi_capabilities


# Statics
NORNIR_CONFIG = "./config.yaml"


# Body
if __name__ == "__main__":
    # Initialise Nornir
    nrn = InitNornir(config_file=NORNIR_CONFIG)

    # Perform action
    result1 = nrn.run(task=gnmi_capabilities)
    result2 = nrn.run(task=gnmi_get, path=["/System/acl-items"])
    print_result(result2)
