llvm/utils/gn/build/run_built_binary.py
=======================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python3
"""Runs a built binary."""

import subprocess
import sys

# Prefix with ./ to run built binary, not arbitrary stuff from PATH.
sys.exit(subprocess.call(['./' + sys.argv[1]] + sys.argv[2:]))


