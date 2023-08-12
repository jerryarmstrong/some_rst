test/BugPoint/compile-custom.ll.py
==================================

Last edited: 2020-02-10 23:18:46

Contents:

.. code-block:: py

    #!/usr/bin/env python

import sys

# Currently any print-out from the custom tool is interpreted as a crash
# (i.e. test is still interesting)

print("Error: " + ' '.join(sys.argv[1:]))

sys.exit(1)


