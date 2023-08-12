llvm/utils/lit/tests/custom-result-category.py
==============================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # UNSUPPORTED: system-windows
# Test lit.main.add_result_category() extension API.

# RUN: not %{lit} %{inputs}/custom-result-category | FileCheck %s

# CHECK: CUSTOM_PASS: custom-result-category :: test1.txt
# CHECK: CUSTOM_FAILURE: custom-result-category :: test2.txt

# CHECK-NOT: My Passed Tests (1)
# CHECK-NOT:   custom-result-category :: test1.txt
# CHECK:     My Failed Tests (1)
# CHECK:       custom-result-category :: test2.txt

# CHECK: My Passed: 1
# CHECK: My Failed: 1


