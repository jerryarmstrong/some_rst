llvm/utils/lit/tests/max-failures.py
====================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # UNSUPPORTED: system-windows

# Check the behavior of --max-failures option.
#
# RUN: not %{lit}                  %{inputs}/max-failures >  %t.out 2>&1
# RUN: not %{lit} --max-failures=1 %{inputs}/max-failures >> %t.out 2>&1
# RUN: not %{lit} --max-failures=2 %{inputs}/max-failures >> %t.out 2>&1
# RUN: not %{lit} --max-failures=0 %{inputs}/max-failures 2>> %t.out
# RUN: FileCheck < %t.out %s
#

# CHECK-NOT: reached maximum number of test failures
# CHECK-NOT: Skipped
# CHECK: Failed: 3

# CHECK: reached maximum number of test failures, skipping remaining tests
# CHECK: Skipped: 2
# CHECK: Failed : 1

# CHECK: reached maximum number of test failures, skipping remaining tests
# CHECK: Skipped: 1
# CHECK: Failed : 2

# CHECK: error: argument --max-failures: requires positive integer, but found '0'


