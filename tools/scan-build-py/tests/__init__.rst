tools/scan-build-py/tests/__init__.py
=====================================

Last edited: 2018-11-26 16:38:37

Contents:

.. code-block:: py

    # -*- coding: utf-8 -*-
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.

import unittest

import tests.unit
import tests.functional.cases


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(tests.unit))
    suite.addTests(loader.loadTestsFromModule(tests.functional.cases))
    return suite


