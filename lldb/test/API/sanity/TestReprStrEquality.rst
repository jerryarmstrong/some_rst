lldb/test/API/sanity/TestReprStrEquality.py
===========================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    """
This is a sanity check that verifies that `repr(sbobject)` and `str(sbobject)`
produce the same string.
"""


import lldb
from lldbsuite.test.lldbtest import *


class TestCase(TestBase):

  NO_DEBUG_INFO_TESTCASE = True

  def test(self):
    self.assertEqual(repr(self.dbg), str(self.dbg))


