lldb/docs/_lldb/__init__.py
===========================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    from unittest.mock import Mock
import sys
import types

# This package acts as a mock implementation of the native _lldb module so
# that generating the LLDB documentation doesn't actually require building all
# of LLDB.
module_name = '_lldb'
sys.modules[module_name] = Mock()


