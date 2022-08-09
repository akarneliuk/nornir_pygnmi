# Example Python script with nornir_pygnmi: gnmi_capabilities task.
## Disclaimer
Please, first of all [read the main README.md explaining the overall concept](https://github.com/akarneliuk/nornir_pygnmi/blob/main/examples/README.md).

## Script
The following script is provided for demonstation purpose without any liability on as-is basis. It was successfully run again Cisco NX-OS 9.3.9 (leveraging Cisco Nexus 9000v).
```python
# Modules
import datetime
from nornir.init_nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pygnmi.tasks import gnmi_capabilities


# Statics
NORNIR_CONFIG = "./config.yaml"


# Body
if __name__ == "__main__":
    # Get initial timestamp
    start_time = datetime.datetime.now()
    print(f"Execition started at {start_time}")

    # Initialise Nornir
    nrn = InitNornir(config_file=NORNIR_CONFIG)

    # Perform action
    result1 = nrn.run(task=gnmi_capabilities)
    print_result(result1)

    # Get final timestamp
    end_time = datetime.datetime.now()
    print(f"Execution took {end_time - start_time} and completed at {end_time}")
```

## Example of execution
This the output of the execution
```
# python main.py 
Execition started at 2022-08-09 17:42:35.908224
Cannot get Subject Alternative Names: No <ObjectIdentifier(oid=2.5.29.17, name=subjectAltName)> extension was found
ssl_target_name_override is applied, should be used for testing only!
gnmi_capabilities***************************************************************
* c-1-s1 ** changed : False ****************************************************
vvvv gnmi_capabilities ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'gnmi_version': '0.5.0',
  'supported_encodings': ['json', 'proto'],
  'supported_models': [ { 'name': 'Cisco-NX-OS-device',
                          'organization': 'Cisco Systems, Inc.',
                          'version': '2022-02-04'},
                        { 'name': 'DME',
                          'organization': 'Cisco Systems, Inc.',
                          'version': ''},
                        { 'name': 'Cisco-NX-OS-Syslog-oper',
                          'organization': 'Cisco Systems, Inc.',
                          'version': '2019-08-15'}]}
^^^^ END gnmi_capabilities ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Execution took 0:00:00.178418 and completed at 2022-08-09 17:42:36.086642
```