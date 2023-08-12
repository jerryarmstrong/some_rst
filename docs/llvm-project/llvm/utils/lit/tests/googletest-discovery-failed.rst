llvm/utils/lit/tests/googletest-discovery-failed.py
===================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # Check for correct error message when discovery of tests fails.
#
# RUN: not %{lit} -v %{inputs}/googletest-discovery-failed > %t.cmd.out
# RUN: FileCheck < %t.cmd.out %s


# CHECK: -- Testing:
# CHECK: Failed Tests (1):
# CHECK:   googletest-discovery-failed :: subdir/OneTest.py/failed_to_discover_tests_from_gtest
# CHECK: Failed: 1


