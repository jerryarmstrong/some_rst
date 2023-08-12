compiler-rt/test/sanitizer_common/ios_commands/iossim_env.py
============================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python3

import os, sys, subprocess


idx = 1
for arg in sys.argv[1:]:
  if not "=" in arg:
    break
  idx += 1
  (argname, argval) = arg.split("=")
  os.environ["SIMCTL_CHILD_" + argname] = argval

exitcode = subprocess.call(sys.argv[idx:])
if exitcode > 125:
  exitcode = 126
sys.exit(exitcode)


