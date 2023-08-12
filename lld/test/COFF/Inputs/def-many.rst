lld/test/COFF/Inputs/def-many.py
================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    import sys

print("EXPORTS")
for i in range(0, int(sys.argv[1])):
  print("f%d=f" % (i))


