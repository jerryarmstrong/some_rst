tests/ui/issues/issue-9968.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-9968.rs

// pretty-expanded FIXME #23616

extern crate issue_9968 as lib;

use lib::{Trait, Struct};

pub fn main()
{
    Struct::init().test();
}


