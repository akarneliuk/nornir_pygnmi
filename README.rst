========================
pyGNMI plugin for Nornir
========================

|project|_ |version|_ |coverage|_ |tag|_ |license|_

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

Release **0.2.0**:

- Added new ``gnmi_subscribe()`` task. It supports all telemery subscription modes; however, from the Nornir perspective, the most benefitial is the ``once`` mode. In this case, the task will return a list containing output of all requested data. Such an approach is recommended by some vendors (e.g., Nokia) to collect huge data sets, which are not fitting into a single ``Get()`` RPC implemented in ``nornir_pygnmi`` as ``gnmi_get()`` task.

Release **0.1.2**:

- Added `examples <https://github.com/akarneliuk/nornir_pygnmi/tree/main/examples>`_.
- Modified communication of the task's status for all tasks.

Release **0.1.1**:

- Added ``gnmi_set()`` task.
- Added placeholders for not-implemented methods.

Release **0.1.0**:

- First alpha release.

(c)2022, karneliuk.com

.. |version| image:: https://img.shields.io/static/v1?label=latest&message=v0.2.0&color=success
.. _version: https://pypi.org/project/nornir_pygnmi/
.. |tag| image:: https://img.shields.io/static/v1?label=status&message=stable&color=success
.. _tag: https://pypi.org/project/nornir_pygnmi/
.. |license| image:: https://img.shields.io/static/v1?label=license&message=BSD-3-clause&color=success
.. _license: https://github.com/akarneliuk/nornir_pygnmi/blob/master/LICENSE.txt
.. |project| image:: https://img.shields.io/badge/akarneliuk%2Fnornir_pygnmi-blueviolet.svg?logo=github&color=success
.. _project: https://github.com/akarneliuk/nornir_pygnmi/
.. |coverage| image:: https://img.shields.io/static/v1?label=coverage&message=0%&color=red
.. _coverage: https://github.com/nedbat/coveragepy