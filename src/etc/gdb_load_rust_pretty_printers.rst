src/etc/gdb_load_rust_pretty_printers.py
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: py

    import gdb
import gdb_lookup
gdb_lookup.register_printers(gdb.current_objfile())


