llvm/utils/lit/tests/show-result-codes.py
=========================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # Test the --show-<result-code> {pass,unsupported,xfail,...} options.
#
# RUN: not %{lit} %{inputs}/show-result-codes                           |  FileCheck %s --check-prefix=NONE
# RUN: not %{lit} %{inputs}/show-result-codes --show-unsupported        |  FileCheck %s --check-prefix=ONE
# RUN: not %{lit} %{inputs}/show-result-codes --show-pass --show-xfail  |  FileCheck %s --check-prefix=MULTIPLE

# Failing tests are always shown
# NONE-NOT: Unsupported Tests (1)
# NONE-NOT: Passed Tests (1)
# NONE-NOT: Expectedly Failed Tests (1)
# NONE:     Failed Tests (1)

# ONE:     Unsupported Tests (1)
# ONE-NOT:     Passed Tests (1)
# ONE-NOT: Expectedly Failed Tests (1)
# ONE:     Failed Tests (1)

# MULTIPLE-NOT: Unsupported Tests (1)
# MULTIPLE:     Passed Tests (1)
# MULTIPLE:     Expectedly Failed Tests (1)
# MULTIPLE:     Failed Tests (1)


