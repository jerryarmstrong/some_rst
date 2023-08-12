unittests/lit_unittest_cfg_utils.py
===================================

Last edited: 2018-11-24 20:57:03

Contents:

.. code-block:: py

    # Put all 64-bit sanitizer tests in the darwin-64bit-sanitizer parallelism
# group. This will only run three of them concurrently.
def darwin_sanitizer_parallelism_group_func(test):
  return "darwin-64bit-sanitizer" if "x86_64" in test.file_path else ""


