tests/rustdoc-ui/const-evalutation-ice.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Just check we don't get an ICE for `N`.

use std::cell::Cell;
use std::mem;

pub struct S {
    s: Cell<usize>
}

pub const N: usize = 0 - (mem::size_of::<S>() != 400) as usize;
//~^ ERROR evaluation of constant value failed


