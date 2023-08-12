tests/ui/extern/auxiliary/issue-80074-macro.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

macro_rules! foo_ { () => {}; }
use foo_ as foo;


