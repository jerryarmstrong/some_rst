lldb/test/Shell/Quit/expect_exit_code.py
========================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python

import subprocess
import sys

args = sys.argv

expected_exit_code = args[1]

args = args[2:]
print("Running " + (" ".join(args)))
real_exit_code = subprocess.call(args)

if str(real_exit_code) != expected_exit_code:
  print("Got exit code %d but expected %s" % (real_exit_code, expected_exit_code))
  exit(1)


