lldb/test/API/dotest.py
=======================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python

if __name__ == "__main__":
    import use_lldb_suite

    import lldbsuite.test
    lldbsuite.test.run_suite()


