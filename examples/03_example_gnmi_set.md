# Example Python script with nornir_pygnmi: gnmi_set task.
## Disclaimer
Please, first of all [read the main README.md explaining the overall concept](https://github.com/akarneliuk/nornir_pygnmi/blob/main/examples/README.md).

## Add/update configuration
### Script
The following script is provided for demonstation purpose without any liability on as-is basis. It was successfully run again Cisco NX-OS 9.3.9 (leveraging Cisco Nexus 9000v).
```python
# Modules
import datetime
from nornir.init_nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pygnmi.tasks import gnmi_get, gnmi_set


# Statics
NORNIR_CONFIG = "./config.yaml"
CONFIG_MSG = [
    (
        "/System/intf-items/lb-items/LbRtdIf-list[id=lo1]",
        {"adminSt": "up"}
    )
]


# Body
if __name__ == "__main__":
    # Get initial timestamp
    start_time = datetime.datetime.now()
    print(f"Execition started at {start_time}")

    # Initialise Nornir
    nrn = InitNornir(config_file=NORNIR_CONFIG)

    # Perform action
    result2 = nrn.run(task=gnmi_get, path=["/System/intf-items/lb-items"], datatype="config")
    print_result(result2)

    result3 = nrn.run(task=gnmi_set, update=CONFIG_MSG)
    print_result(result3)

    result4 = nrn.run(task=gnmi_get, path=["/System/intf-items/lb-items"], datatype="config")
    print_result(result4)

    # Get final timestamp
    end_time = datetime.datetime.now()
    print(f"Execution took {end_time - start_time} and completed at {end_time}")
```

### Example of execution
This the output of the execution
```
# python main.py 
Execition started at 2022-08-09 17:56:52.745027
Cannot get Subject Alternative Names: No <ObjectIdentifier(oid=2.5.29.17, name=subjectAltName)> extension was found
ssl_target_name_override is applied, should be used for testing only!
gnmi_get************************************************************************
* c-1-s1 ** changed : False ****************************************************
vvvv gnmi_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'notification': [ { 'alias': None,
                      'atomic': False,
                      'prefix': None,
                      'timestamp': 1660067252611179076,
                      'update': [ { 'path': 'System/intf-items/lb-items',
                                    'val': { 'LbRtdIf-list': [ { 'adminSt': 'up',
                                                                 'id': 'lo0',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}}]}}]}]}
^^^^ END gnmi_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gnmi_set************************************************************************
* c-1-s1 ** changed : True *****************************************************
vvvv gnmi_set ** changed : True vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'prefix': None,
  'response': [ { 'op': 'UPDATE',
                  'path': 'System/intf-items/lb-items/LbRtdIf-list[id=lo1]'}],
  'timestamp': 1660067252837352425}
^^^^ END gnmi_set ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gnmi_get************************************************************************
* c-1-s1 ** changed : False ****************************************************
vvvv gnmi_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'notification': [ { 'alias': None,
                      'atomic': False,
                      'prefix': None,
                      'timestamp': 1660067252937261610,
                      'update': [ { 'path': 'System/intf-items/lb-items',
                                    'val': { 'LbRtdIf-list': [ { 'adminSt': 'up',
                                                                 'id': 'lo0',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}},
                                                               { 'adminSt': 'up',
                                                                 'id': 'lo1',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}}]}}]}]}
^^^^ END gnmi_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Execution took 0:00:00.671899 and completed at 2022-08-09 17:56:53.416926
```

## Delete configuration
### Script
The following script is provided for demonstation purpose without any liability on as-is basis. It was successfully run again Cisco NX-OS 9.3.9 (leveraging Cisco Nexus 9000v).
```python
# Modules
import datetime
from nornir.init_nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pygnmi.tasks import gnmi_get, gnmi_set


# Statics
NORNIR_CONFIG = "./config.yaml"
CONFIG_MSG = ["/System/intf-items/lb-items/LbRtdIf-list[id=lo1]"]


# Body
if __name__ == "__main__":
    # Get initial timestamp
    start_time = datetime.datetime.now()
    print(f"Execition started at {start_time}")

    # Initialise Nornir
    nrn = InitNornir(config_file=NORNIR_CONFIG)

    # Perform action
    result2 = nrn.run(task=gnmi_get, path=["/System/intf-items/lb-items"], datatype="config")
    print_result(result2)

    result3 = nrn.run(task=gnmi_set, delete=CONFIG_MSG)
    print_result(result3)

    result4 = nrn.run(task=gnmi_get, path=["/System/intf-items/lb-items"], datatype="config")
    print_result(result4)

    # Get final timestamp
    end_time = datetime.datetime.now()
    print(f"Execution took {end_time - start_time} and completed at {end_time}")
```

### Example of execution
This the output of the execution
```
# python main.py 

Execition started at 2022-08-09 17:59:05.973442
Cannot get Subject Alternative Names: No <ObjectIdentifier(oid=2.5.29.17, name=subjectAltName)> extension was found
ssl_target_name_override is applied, should be used for testing only!
gnmi_get************************************************************************
* c-1-s1 ** changed : False ****************************************************
vvvv gnmi_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'notification': [ { 'alias': None,
                      'atomic': False,
                      'prefix': None,
                      'timestamp': 1660067385717885989,
                      'update': [ { 'path': 'System/intf-items/lb-items',
                                    'val': { 'LbRtdIf-list': [ { 'adminSt': 'up',
                                                                 'id': 'lo0',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}},
                                                               { 'adminSt': 'up',
                                                                 'id': 'lo1',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}}]}}]}]}
^^^^ END gnmi_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gnmi_set************************************************************************
* c-1-s1 ** changed : True *****************************************************
vvvv gnmi_set ** changed : True vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'prefix': None,
  'response': [ { 'op': 'DELETE',
                  'path': 'System/intf-items/lb-items/LbRtdIf-list[id=lo1]'}],
  'timestamp': 1660067385842283616}
^^^^ END gnmi_set ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gnmi_get************************************************************************
* c-1-s1 ** changed : False ****************************************************
vvvv gnmi_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'notification': [ { 'alias': None,
                      'atomic': False,
                      'prefix': None,
                      'timestamp': 1660067385946676764,
                      'update': [ { 'path': 'System/intf-items/lb-items',
                                    'val': { 'LbRtdIf-list': [ { 'adminSt': 'up',
                                                                 'id': 'lo0',
                                                                 'linkLog': 'default',
                                                                 'rtvrfMbr-items': { 'tDn': "/System/inst-items/Inst-list[name='default']"}}]}}]}]}
^^^^ END gnmi_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Execution took 0:00:00.477407 and completed at 2022-08-09 17:59:06.450849
```