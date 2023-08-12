tests/ui/imports/issue-45829/rename.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use core;
use std as core;
//~^ ERROR is defined multiple times

fn main() {
    1 + 1;
}


