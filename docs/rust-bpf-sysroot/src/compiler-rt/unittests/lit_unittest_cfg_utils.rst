src/compiler-rt/unittests/lit_unittest_cfg_utils.py
===================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    # Put all 64-bit tests in the shadow-memory parallelism group. We throttle those
# in our common lit config (lit.common.unit.cfg.py).
def darwin_sanitizer_parallelism_group_func(test):
  return "shadow-memory" if "x86_64" in test.file_path else None


