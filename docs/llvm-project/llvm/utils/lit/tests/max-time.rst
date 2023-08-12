llvm/utils/lit/tests/max-time.py
================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # UNSUPPORTED: system-windows

# Test overall lit timeout (--max-time).
#
# RUN: %{lit} %{inputs}/max-time --max-time=5 2>&1  |  FileCheck %s

# CHECK: reached timeout, skipping remaining tests
# CHECK: Skipped: 1
# CHECK: Passed : 1


