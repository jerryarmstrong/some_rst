tests/run-make-fulldeps/save-analysis-rfc2126/validate_json.py
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: py

    #!/usr/bin/env python

import sys
import json

crates = json.loads(sys.stdin.readline().strip())["prelude"]["external_crates"]
assert any(map(lambda c: c["id"]["name"] == "krate2", crates))


