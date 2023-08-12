tests/ui/imports/issue-26873-multifile/mod.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
mod A;

use self::A::*;


