lldb/test/API/types/TestDoubleTypes.py
======================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    """
Test that variables of floating point types are displayed correctly.
"""



import AbstractBase

import lldb
from lldbsuite.test.decorators import *
from lldbsuite.test.lldbtest import *
from lldbsuite.test import lldbutil


class DoubleTypesTestCase(AbstractBase.GenericTester):

    def test_double_type(self):
        """Test that double-type variables are displayed correctly."""
        self.build_and_run('double.cpp', set(['double']))

    @skipUnlessDarwin
    def test_double_type_from_block(self):
        """Test that double-type variables are displayed correctly from a block."""
        self.build_and_run('double.cpp', set(['double']), bc=True)


