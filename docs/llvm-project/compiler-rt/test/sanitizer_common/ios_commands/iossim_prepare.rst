compiler-rt/test/sanitizer_common/ios_commands/iossim_prepare.py
================================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python3

import json

print(json.dumps({"env": {}}))


