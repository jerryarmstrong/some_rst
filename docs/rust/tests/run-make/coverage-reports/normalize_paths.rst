tests/run-make/coverage-reports/normalize_paths.py
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: py

    #!/usr/bin/env python

from __future__ import print_function

import sys

# Normalize file paths in output
for line in sys.stdin:
    if line.startswith("..") and line.rstrip().endswith(".rs:"):
        print(line.replace("\\", "/"), end='')
    else:
        print(line, end='')


