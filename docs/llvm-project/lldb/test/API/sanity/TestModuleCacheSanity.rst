lldb/test/API/sanity/TestModuleCacheSanity.py
=============================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    """
This is a sanity check that verifies that the module cache path is set
correctly and points inside the default test build directory.
"""


import lldb
import lldbsuite.test.lldbutil as lldbutil
from lldbsuite.test.lldbtest import *


class ModuleCacheSanityTestCase(TestBase):

  NO_DEBUG_INFO_TESTCASE = True

  def test(self):
    self.expect(
        'settings show symbols.clang-modules-cache-path',
        substrs=['lldb-test-build.noindex', 'module-cache-lldb'])


