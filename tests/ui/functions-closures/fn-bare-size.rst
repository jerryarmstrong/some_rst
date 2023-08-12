tests/ui/functions-closures/fn-bare-size.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::mem;

pub fn main() {
    // Bare functions should just be a pointer
    assert_eq!(mem::size_of::<extern "Rust" fn()>(), mem::size_of::<isize>());
}


