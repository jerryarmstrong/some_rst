lldb/test/API/test_utils/TestDecorators.py
==========================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    from lldbsuite.test.lldbtest import Base
from lldbsuite.test.decorators import *


class TestDecorators(Base):
    NO_DEBUG_INFO_TESTCASE = True

    @expectedFailureAll(debug_info="dwarf")
    def test_decorator_skip_no_debug_info(self):
        """Test that specifying a debug info category works for a NO_DEBUG_INFO_TESTCASE"""
        pass


