llvm/utils/lit/tests/lld-features.py
====================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    ## Show that each of the LLD variants detected by use_lld comes with its own
## feature.

# RUN: %{lit} %{inputs}/lld-features 2>&1 | FileCheck %s -DDIR=%p

# CHECK: Passed: 4


