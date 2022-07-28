# Sample Network Automation Project leveraging Nornir and Nornir_pygnmi
This directory contains an example of network automation project using GNMI/YANG framework leveraging `nornir` and `nornir_pygnmi`.

## Requirements
The following requirements are used for such a project:
```
nornir_pygnmi
nornir_utils
```

Install them as normally:
```
$ pip install -r requirements.txt
```

## Directory structure
The structure of your network automation project leveraging `nornir_pygnmi` is pretty standard for Nornir (for simplicity, we show default inventory plugin with local YAML files):
```
+--certs
|  +--device_cert.pem
+--inventory
|  +--hosts.yaml
+--config.yaml
+--main.py
```

What is not standard for Nornir is the `certs` directory, which stores SSL certificates you would use to authenticate against network devices. For some network operating systems (e.g., `Arista EOS`) it is possible to automatically retrieve the certificate from the network device itself; hence, this folder would be not needed. At the same time, other network operating systems (e.g., `Cisco NX-OS`) doesn't allow you to do so, and you, therefore, would need to download certificate from the network device and put in such a directory.

*You may think about different hierarchy of directories, we just suggest you a nice starting point for your nornir_pygnmi journey.*

## Config files
The config file `config.yaml` is absolutely standard for Nornir and no mentions about `nornir_pygnmi` is needed there:
```yaml
---
inventory:
    plugin: SimpleInventory
    options:
        host_file: "./inventory/hosts.yaml"
        group_file: "./inventory/groups.yaml"
        defaults_file: "./inventory/defaults.yaml"

logging:
    enabled: True
    log_file: "./log/nornir.log"

runner:
    plugin: threaded
    options:
        num_workers: 20
...
```

## Invenvoty
In the `connectivity_options` of the host you need to specify at least `pygnmi: {}` if you don't need providing any extra arguments. 
```yaml
---
dev-pygnmi-nxos1:
  hostname: 192.168.101.20
  port: 50051
  connection_options:
    pygnmi:
      extras:
        path_cert: "./certs/dev-pygnmi-nxos1.pem"
        skip_verify: True
...
```

### Pygnmi arguments
If you need, specify `extras` context and add there all key-value pairs you would normally provide to `gNMIclient()` class of `pygnmi` library. [See pygnmi documentation for further reference](https://github.com/akarneliuk/pygnmi).

## Nornir script
Sample Python script leveraging `nornir_pygnmi`:
```python
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
    print_result(result1)
    print_result(result2)
```

## Execution

```
# python main.py 
Execition started at 2022-07-27 17:28:16.563370
Cannot get Subject Alternative Names: No <ObjectIdentifier(oid=2.5.29.17, name=subjectAltName)> extension was found
ssl_target_name_override is applied, should be used for testing only!
gnmi_capabilities***************************************************************
* dev-pygnmi-nxos1 ** changed : False ******************************************
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
gnmi_get************************************************************************
* dev-pygnmi-nxos1 ** changed : False ******************************************
vvvv gnmi_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'notification': [ { 'alias': None,
                      'atomic': False,
                      'prefix': None,
                      'timestamp': 1658942381901249226,
                      'update': [ { 'path': 'System/acl-items',
                                    'val': { 'ipv4-items': { 'name-items': { 'ACL-list': [ { 'configStatus': 0,
                                                                                             'ignRoutable': False,
                                                                                             'name': 'ACL_IPV4_RP_RANGES_NORMAL',
                                                                                             'perACEStatistics': 0,
                                                                                             'seq-items': { 'ACE-list': [ { 'ack': False,
                                                                                                                            'action': 'permit',
                                                                                                                            'captureSession': 0,
                                                                                                                            'configStatus': 0,
                                                                                                                            'dstPort1': 0,
                                                                                                                            'dstPort2': 0,
                                                                                                                            'dstPortMask': 0,
                                                                                                                            'dstPortOp': 'none',
                                                                                                                            'dstPrefix': '239.0.0.0',
                                                                                                                            'dstPrefixLength': 8,
                                                                                                                            'est': False,
                                                                                                                            'fin': False,
                                                                                                                            'fragment': False,
                                                                                                                            'httpOption': 'invalid',
                                                                                                                            'icmpCode': 256,
                                                                                                                            'icmpStr': 256,
                                                                                                                            'icmpType': 256,
                                                                                                                            'igmpType': 16,
                                                                                                                            'logging': False,
                                                                                                                            'pktLen1': 19,
                                                                                                                            'pktLen2': 19,
                                                                                                                            'pktLenOp': 'none',
                                                                                                                            'precedence': 8,
                                                                                                                            'protocol': 0,
                                                                                                                            'protocolMask': 255,
                                                                                                                            'psh': False,
                                                                                                                            'rev': False,
                                                                                                                            'rst': False,
                                                                                                                            'seqNum': 20,
                                                                                                                            'srcPort1': 0,
                                                                                                                            'srcPort2': 0,
                                                                                                                            'srcPortMask': 0,
                                                                                                                            'srcPortOp': 'none',
                                                                                                                            'srcPrefix': '0.0.0.0',
                                                                                                                            'srcPrefixLength': 0,
                                                                                                                            'syn': False,
                                                                                                                            'tcpFlagsMask': 0,
                                                                                                                            'tcpOptionLength': 41,
                                                                                                                            'telemetryPath': False,
                                                                                                                            'telemetryQueue': False,
                                                                                                                            'tos': 0,
                                                                                                                            'urg': False,
                                                                                                                            'vlan': 4095,
                                                                                                                            'vni': 16777216},
                                                                                                                          { 'ack': False,
                                                                                                                            'action': 'permit',
                                                                                                                            'captureSession': 0,
                                                                                                                            'configStatus': 0,
                                                                                                                            'dstPort1': 0,
                                                                                                                            'dstPort2': 0,
                                                                                                                            'dstPortMask': 0,
                                                                                                                            'dstPortOp': 'none',
                                                                                                                            'dstPrefix': '237.0.0.0',
                                                                                                                            'dstPrefixLength': 8,
                                                                                                                            'est': False,
                                                                                                                            'fin': False,
                                                                                                                            'fragment': False,
                                                                                                                            'httpOption': 'invalid',
                                                                                                                            'icmpCode': 256,
                                                                                                                            'icmpStr': 256,
                                                                                                                            'icmpType': 256,
                                                                                                                            'igmpType': 16,
                                                                                                                            'logging': False,
                                                                                                                            'pktLen1': 19,
                                                                                                                            'pktLen2': 19,
                                                                                                                            'pktLenOp': 'none',
                                                                                                                            'precedence': 8,
                                                                                                                            'protocol': 0,
                                                                                                                            'protocolMask': 255,
                                                                                                                            'psh': False,
                                                                                                                            'rev': False,
                                                                                                                            'rst': False,
                                                                                                                            'seqNum': 10,
                                                                                                                            'srcPort1': 0,
                                                                                                                            'srcPort2': 0,
                                                                                                                            'srcPortMask': 0,
                                                                                                                            'srcPortOp': 'none',
                                                                                                                            'srcPrefix': '0.0.0.0',
                                                                                                                            'srcPrefixLength': 0,
                                                                                                                            'syn': False,
                                                                                                                            'tcpFlagsMask': 0,
                                                                                                                            'tcpOptionLength': 41,
                                                                                                                            'telemetryPath': False,
                                                                                                                            'telemetryQueue': False,
                                                                                                                            'tos': 0,
                                                                                                                            'urg': False,
                                                                                                                            'vlan': 4095,
                                                                                                                            'vni': 16777216}]}},
                                                                                           { 'configStatus': 0,
                                                                                             'ignRoutable': False,
                                                                                             'name': 'ACL_IPV4_RP_RANGES_BIDIR',
                                                                                             'perACEStatistics': 0,
                                                                                             'seq-items': { 'ACE-list': [ { 'ack': False,
                                                                                                                            'action': 'permit',
                                                                                                                            'captureSession': 0,
                                                                                                                            'configStatus': 0,
                                                                                                                            'dstPort1': 0,
                                                                                                                            'dstPort2': 0,
                                                                                                                            'dstPortMask': 0,
                                                                                                                            'dstPortOp': 'none',
                                                                                                                            'dstPrefix': '238.0.0.0',
                                                                                                                            'dstPrefixLength': 8,
                                                                                                                            'est': False,
                                                                                                                            'fin': False,
                                                                                                                            'fragment': False,
                                                                                                                            'httpOption': 'invalid',
                                                                                                                            'icmpCode': 256,
                                                                                                                            'icmpStr': 256,
                                                                                                                            'icmpType': 256,
                                                                                                                            'igmpType': 16,
                                                                                                                            'logging': False,
                                                                                                                            'pktLen1': 19,
                                                                                                                            'pktLen2': 19,
                                                                                                                            'pktLenOp': 'none',
                                                                                                                            'precedence': 8,
                                                                                                                            'protocol': 0,
                                                                                                                            'protocolMask': 255,
                                                                                                                            'psh': False,
                                                                                                                            'rev': False,
                                                                                                                            'rst': False,
                                                                                                                            'seqNum': 10,
                                                                                                                            'srcPort1': 0,
                                                                                                                            'srcPort2': 0,
                                                                                                                            'srcPortMask': 0,
                                                                                                                            'srcPortOp': 'none',
                                                                                                                            'srcPrefix': '0.0.0.0',
                                                                                                                            'srcPrefixLength': 0,
                                                                                                                            'syn': False,
                                                                                                                            'tcpFlagsMask': 0,
                                                                                                                            'tcpOptionLength': 41,
                                                                                                                            'telemetryPath': False,
                                                                                                                            'telemetryQueue': False,
                                                                                                                            'tos': 0,
                                                                                                                            'urg': False,
                                                                                                                            'vlan': 4095,
                                                                                                                            'vni': 16777216}]}}]}}}}]}]}
^^^^ END gnmi_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```