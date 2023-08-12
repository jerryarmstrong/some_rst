tests/ui/imports/issue-26873-multifile/A/C.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use super::*;

use super::B::S;

pub struct T { i: i32 }


