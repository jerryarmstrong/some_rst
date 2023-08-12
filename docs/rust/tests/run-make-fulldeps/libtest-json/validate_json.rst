tests/run-make-fulldeps/libtest-json/validate_json.py
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: py

    #!/usr/bin/env python

import sys
import json

# Try to decode line in order to ensure it is a valid JSON document
for line in sys.stdin:
    json.loads(line)


