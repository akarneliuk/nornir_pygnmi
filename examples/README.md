# Sample Network Automation Project leveraging Nornir and Nornir_pygnmi
This directory contains examples

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
  data:
...
```

### Pygnmi arguments
If you need, specify `extras` context and add there all key-value pairs you would normally provide to `gNMIclient()` class of `pygnmi` library. [See pygnmi documentation for further reference](https://github.com/akarneliuk/pygnmi).

## Nornir script

## Execution