========================
pyGNMI plugin for Nornir
========================
This repository contains GNMI plugin for Nornir leveraging pyGNMI library

=====
Usage
=====
Sample code example:

.. code-block:: python3

  # Modules
  from nornir.init_nornir import InitNornir
  from nornir_utils.plugins.functions import print_result
  from nornir_pygnmi.tasks import gnmi_capabilities

  # Statics
  NORNIR_CONFIG = "./config.yaml"

  # Body
  if __name__ == "__main__":
      # Initialise Nornir
      nrn = InitNornir(config_file=NORNIR_CONFIG)

      # Run task
      result1 = nrn.run(task=gnmi_capabilities)
      print_result(result1)

Installation
------------

.. code-block:: bash

  pip install nornir_pygnmi

=======
Dev Log
=======

Release **0.1.2**:

- Added `examples <https://github.com/akarneliuk/nornir_pygnmi/tree/main/examples>`_.
- Modified communication of the task's status for all tasks.

Release **0.1.1**:

- Added ``gnmi_set()`` task.
- Added placeholders for not-implemented methods.

Release **0.1.0**:

- First alpha release.

(c)2022, karneliuk.com