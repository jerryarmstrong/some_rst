tests/ui/sepcomp/sepcomp-fns-backwards.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// compile-flags: -C codegen-units=3

// Test references to items that haven't been codegened yet.

// Generate some code in the first compilation unit before declaring any
// modules.  This ensures that the first module doesn't go into the same
// compilation unit as the top-level module.

fn pad() -> usize { 0 }

mod b {
    pub fn three() -> usize {
        ::one() + ::a::two()
    }
}

mod a {
    pub fn two() -> usize {
        ::one() + ::one()
    }
}

fn one() -> usize {
    1
}

fn main() {
    assert_eq!(one(), 1);
    assert_eq!(a::two(), 2);
    assert_eq!(b::three(), 3);
}


